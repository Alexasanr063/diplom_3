import requests
import allure
from diplom_3.config import API_ENDPOINTS, TEST_DATA


class BurgerAPIClient:
    """API клиент для работы с бургерной"""

    def __init__(self, auth_token=None):
        self.headers = {
            "Content-Type": "application/json",
            "X-API-Version": "1.0"
        }
        if auth_token:
            self.headers["Authorization"] = f"Bearer {auth_token}"

    def set_auth_token(self, auth_token):
        """Установить токен авторизации"""
        if auth_token:
            self.headers["Authorization"] = f"Bearer {auth_token}"
        elif "Authorization" in self.headers:
            del self.headers["Authorization"]

    @allure.step("API: Получение списка ингредиентов")
    def get_ingredients_list(self):
        """Получить все доступные ингредиенты"""
        response = requests.get(
            API_ENDPOINTS["ingredients"],
            headers=self.headers,
            timeout=10
        )
        return response

    @allure.step("API: Создание заказа")
    def create_burger_order(self, ingredients):
        """Создать новый заказ с указанными ингредиентами"""
        order_data = {"ingredients": ingredients}
        response = requests.post(
            API_ENDPOINTS["orders"],
            json=order_data,
            headers=self.headers,
            timeout=15
        )
        return response

    @allure.step("API: Получение заказов пользователя")
    def get_user_orders_history(self):
        """Получить историю заказов авторизованного пользователя"""
        response = requests.get(
            API_ENDPOINTS["orders"],
            headers=self.headers,
            timeout=8
        )
        return response

    @allure.step("API: Получение заказа по номеру")
    def get_order_by_id(self, order_id):
        """Получить детали заказа по идентификатору"""
        response = requests.get(
            f"{API_ENDPOINTS['orders']}/{order_id}",
            headers=self.headers,
            timeout=10
        )
        return response

    @allure.step("API: Получение всех заказов")
    def get_all_orders_feed(self):
        """Получить ленту всех заказов"""
        response = requests.get(
            API_ENDPOINTS["orders_all"],
            headers=self.headers,
            timeout=12
        )
        return response

    @allure.step("API: Создание тестового заказа")
    def create_test_order(self):
        """Создать тестовый заказ с предустановленными ингредиентами"""
        test_ingredients = TEST_DATA["ingredient_ids"]
        return self.create_burger_order(test_ingredients)

    def is_authenticated(self):
        """Проверить наличие авторизации"""
        return "Authorization" in self.headers