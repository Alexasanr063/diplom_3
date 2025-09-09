import requests
import allure
from diplom_3.config import API_ENDPOINTS, TEST_DATA, MESSAGES


class BurgerOrderAPI:
    """API клиент для управления заказами в Stellar Burgers"""

    def __init__(self, auth_token=None):
        self.base_headers = {
            "Content-Type": "application/json",
            "User-Agent": "StellarBurgers-API-Client/1.0"
        }
        if auth_token:
            self.base_headers["Authorization"] = f"Bearer {auth_token}"

    @allure.step("API: Получение списка ингредиентов")
    def fetch_ingredients(self):
        """Получить все доступные ингредиенты для бургеров"""
        try:
            response = requests.get(
                API_ENDPOINTS["ingredients"],
                headers=self.base_headers,
                timeout=10
            )
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            allure.attach(f"Ошибка получения ингредиентов: {str(e)}", name="API Error")
            raise

    @allure.step("API: Создание нового заказа")
    def place_order(self, ingredients_list):
        """Создать новый заказ с указанными ингредиентами"""
        order_payload = {
            "ingredients": ingredients_list
        }

        try:
            response = requests.post(
                API_ENDPOINTS["orders"],
                json=order_payload,
                headers=self.base_headers,
                timeout=15
            )
            return response
        except requests.exceptions.Timeout:
            allure.attach("Таймаут при создании заказа", name="Timeout Error")
            raise Exception("Превышено время ожидания создания заказа")

    @allure.step("API: Получение заказов пользователя")
    def get_customer_orders(self):
        """Получить истории заказов текущего пользователя"""
        try:
            response = requests.get(
                API_ENDPOINTS["orders"],
                headers=self.base_headers,
                timeout=8
            )
            return response
        except requests.exceptions.ConnectionError:
            allure.attach("Ошибка соединения при получении заказов", name="Connection Error")
            raise

    @allure.step("API: Получение деталей заказа по номеру")
    def get_order_details(self, order_number):
        """Получить детальную информацию о заказе по его номеру"""
        try:
            response = requests.get(
                f"{API_ENDPOINTS['orders']}/{order_number}",
                headers=self.base_headers,
                timeout=10
            )
            return response
        except requests.exceptions.RequestException as e:
            allure.attach(f"Ошибка получения заказа {order_number}: {str(e)}", name="API Error")
            raise

    @allure.step("API: Получение ленты всех заказов")
    def get_orders_feed(self):
        """Получить публичную ленту всех заказов"""
        try:
            response = requests.get(
                API_ENDPOINTS["orders_all"],
                headers=self.base_headers,
                timeout=12
            )
            response.raise_for_status()
            return response
        except requests.exceptions.HTTPError as e:
            allure.attach(f"HTTP ошибка в ленте заказов: {e.response.status_code}", name="HTTP Error")
            raise

    @allure.step("API: Создание тестового заказа")
    def create_sample_order(self):
        """Создать тестовый заказ с предопределенными ингредиентами"""
        sample_ingredients = TEST_DATA["ingredient_ids"][:2]  # Берем первые два ингредиента
        return self.place_order(sample_ingredients)

    @allure.step("API: Проверка статуса аутентификации")
    def check_auth_status(self):
        """Проверить, аутентифицирован ли клиент"""
        return "Authorization" in self.base_headers

    def set_auth_token(self, token):
        """Установить токен аутентификации"""
        if token:
            self.base_headers["Authorization"] = f"Bearer {token}"
        elif "Authorization" in self.base_headers:
            del self.base_headers["Authorization"]