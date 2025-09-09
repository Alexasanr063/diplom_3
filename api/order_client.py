import requests
import allure
from diplom_3.config import API_ENDPOINTS, TEST_DATA


class OrderAPI:
    # API клиент для операций с заказами

    def __init__(self, access_token=None):
        self.headers = {"Content-Type": "application/json"}
        if access_token:
            self.headers["Authorization"] = access_token

    def set_auth_token(self, access_token):
        # Установить токен авторизации для аутентифицированных запросов
        if access_token:
            self.headers["Authorization"] = access_token
        elif "Authorization" in self.headers:
            del self.headers["Authorization"]

    @allure.step("API: Получение ингредиентов")
    def get_ingredients(self):
        # Получить все доступные ингредиенты
        response = requests.get(API_ENDPOINTS["ingredients"], headers=self.headers)
        return response

    @allure.step("API: Создание заказа")
    def create_order(self, ingredient_ids):
        # Создать новый заказ с указанными ID ингредиентов
        order_data = {"ingredients": ingredient_ids}
        response = requests.post(
            API_ENDPOINTS["orders"], json=order_data, headers=self.headers
        )
        return response

    @allure.step("API: Получение заказов пользователя")
    def get_user_orders(self):
        # Получить заказы для аутентифицированного пользователя
        response = requests.get(API_ENDPOINTS["orders"], headers=self.headers)
        return response

    @allure.step("API: Получение заказа по номеру")
    def get_order_by_number(self, order_number):
        # Получить детали заказа по номеру заказа
        response = requests.get(
            f"{API_ENDPOINTS['orders']}/{order_number}", headers=self.headers
        )
        return response

    @allure.step("API: Получение всех заказов (лента)")
    def get_all_orders(self):
        # Получить все заказы из публичной ленты
        response = requests.get(API_ENDPOINTS["orders_all"], headers=self.headers)
        return response

    @allure.step("API: Создание тестового заказа с ингредиентами по умолчанию")
    def create_test_order(self):
        # Создать тестовый заказ с предопределенными ингредиентами
        # Использовать предопределенные ID тестовых ингредиентов из конфига
        test_ingredients = TEST_DATA["ingredient_ids"]
        return self.create_order(test_ingredients)

    def is_authenticated(self):
        # Проверить наличие токена аутентификации у API клиента
        return "Authorization" in self.headers