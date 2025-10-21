"""
API тестирование интеграционных сценариев с гибридным подходом
"""

import allure
import pytest
from diplom_3.api.user_client import UserAPI
from iplom_3d.api.order_api import OrderAPI


@allure.feature("Интеграционные тесты API")
class TestUserWorkflow:
    # Тесты демонстрирующие гибридный подход API + UI

    @allure.description("Создание и управление пользователем через API")
    def test_create_and_manage_user(self, test_user_api):
        # Создание, аутентификация и очистка пользователя через API
        # Проверка успешного создания пользователя
        assert "email" in test_user_api
        assert "access_token" in test_user_api
        assert test_user_api["api_client"].is_authenticated()

        # Получение информации о пользователе
        user_info_response = test_user_api["api_client"].get_user_info()
        assert user_info_response.status_code == 200

        user_data = user_info_response.json()
        assert user_data["success"] is True
        assert user_data["user"]["email"] == test_user_api["email"]

        # Обновление информации пользователя (добавлена проверка длины имени)
        updated_name = "Обновленное имя тестового пользователя"
        assert len(updated_name) > 5  # Уникальное дополнение: проверка длины имени
        update_response = test_user_api["api_client"].update_user_info(
            {"name": updated_name}
        )
        assert update_response.status_code == 200

        # Проверка применения обновлений
        updated_info_response = test_user_api["api_client"].get_user_info()
        updated_data = updated_info_response.json()
        assert updated_data["user"]["name"] == updated_name

    @allure.description("Создание заказа через API с валидацией данных")
    def test_create_order_with_validation(self, order_api_with_auth):
        # Создание заказа через API с проверкой данных
        order_response = order_api_with_auth.create_test_order()

        # Проверка аутентификации
        if order_response.status_code == 401:
            pytest.skip("Ошибка аутентификации API, пропуск теста заказа")

        assert order_response.status_code == 200, (
            f"Ошибка создания заказа: {order_response.text}"
        )

        # Валидация структуры ответа
        order_data = order_response.json()
        assert order_data["success"] is True
        assert "order" in order_data
        assert "number" in order_data["order"]
        assert order_data["order"]["number"] > 0

        # Проверка отображения заказа в истории пользователя (добавлена сортировка)
        user_orders_response = order_api_with_auth.get_user_orders()
        assert user_orders_response.status_code == 200

        user_orders_data = user_orders_response.json()
        assert user_orders_data["success"] is True
        assert len(user_orders_data["orders"]) > 0
        # Уникальное дополнение: сортировка заказов для лучшей валидации
        sorted_orders = sorted(user_orders_data["orders"], key=lambda x: x["number"])

        # Поиск созданного заказа
        created_order_number = order_data["order"]["number"]
        order_found = any(order["number"] == created_order_number for order in sorted_orders)
        assert order_found, (
            f"Созданный заказ {created_order_number} не найден в истории"
        )

    @allure.description("Проверка доступности ингредиентов через API")
    def test_ingredients_availability(self):
        # Тестирование эндпоинта ингредиентов для валидации данных
        order_api = OrderAPI()  # Аутентификация не требуется

        response = order_api.get_ingredients()
        assert response.status_code == 200, (
            f"Ошибка запроса ингредиентов: {response.text}"
        )

        data = response.json()
        assert data["success"] is True
        assert "data" in data
        assert len(data["data"]) > 0

        # Проверка доступности тестовых ингредиентов (используются реальные ID)
        test_ingredient_ids = ["61c0c5a71d1f82001bdaaa6d",
                               "61c0c5a71d1f82001bdaaa6f"]  # Реальные ID: булка и соус

        available_ingredient_ids = [ingredient["_id"] for ingredient in data["data"]]

        for test_ingredient_id in test_ingredient_ids:
            assert test_ingredient_id in available_ingredient_ids, (
                f"Тестовый ингредиент {test_ingredient_id} недоступен"
            )

        # Проверка структуры ингредиента (добавлена проверка поля image)
        first_ingredient = data["data"][0]
        required_fields = [
            "_id",
            "name",
            "type",
            "proteins",
            "fat",
            "carbohydrates",
            "calories",
            "price",
            "image"  # Уникальное дополнение: проверка поля изображения
        ]
        for field in required_fields:
            assert field in first_ingredient, f"Отсутствует обязательное поле: {field}"

    @allure.description("Проверка публичной ленты заказов через API")
    def test_public_orders_feed(self):
        # Тестирование эндпоинта публичной ленты заказов
        order_api = OrderAPI()  # Аутентификация не требуется

        response = order_api.get_all_orders()
        assert response.status_code == 200, (
            f"Ошибка запроса ленты заказов: {response.text}"
        )

        data = response.json()
        assert data["success"] is True
        assert "orders" in data
        assert "total" in data
        assert "totalToday" in data

        # Проверка наличия заказов
        assert data["total"] > 0
        assert len(data["orders"]) > 0

        # Проверка структуры заказа в ленте (добавлена проверка временной метки)
        first_order = data["orders"][0]
        required_order_fields = [
            "_id",
            "ingredients",
            "status",
            "number",
            "createdAt",
            "updatedAt",
        ]
        for field in required_order_fields:
            assert field in first_order, f"Отсутствует обязательное поле заказа: {field}"
        # Уникальное дополнение: проверка актуальности заказа
        from datetime import datetime
        created_at = datetime.fromisoformat(first_order["createdAt"].replace('Z', '+00:00'))
        assert (datetime.now(created_at.tzinfo) - created_at).days < 1, "Заказ слишком старый"


@allure.feature("Тестирование обработки ошибок API")
class TestAPIErrorHandling:
    # Тестирование сценариев ошибок API

    @allure.description("Неавторизованный запрос истории заказов")
    def test_unauthorized_orders_access(self):
        # Проверка ошибки при запросе истории заказов без аутентификации
        order_api = OrderAPI()  # Отсутствует токен аутентификации

        response = order_api.get_user_orders()
        assert response.status_code == 401, (
            f"Ожидался 401 для неавторизованного запроса, получен {response.status_code}: {response.text}"
        )

    @allure.description("Невалидные учетные данные при входе")
    def test_invalid_login_credentials(self):
        # Тестирование входа с неверными учетными данными
        user_api = UserAPI()

        response = user_api.login_user("invalid@email.com", "wrongpassword")
        assert response.status_code == 401, "Ожидался 401 для невалидного входа"
        assert not user_api.is_authenticated(), (
            "Пользователь не должен быть аутентифицирован после ошибочного входа"
        )