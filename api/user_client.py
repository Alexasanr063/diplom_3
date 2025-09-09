import requests
import allure
from diplom_3.config import API_ENDPOINTS, TEST_USER, MESSAGES


class UserAPI:
    # API клиент для операций с пользователями

    def __init__(self):
        self.base_url = API_ENDPOINTS["register"].replace("/auth/register", "")
        self.headers = {"Content-Type": "application/json"}
        self.access_token = None
        self.refresh_token = None

    @allure.step("API: Регистрация пользователя")
    def register_user(self, user_data):
        # Регистрация нового пользователя
        response = requests.post(
            API_ENDPOINTS["register"], json=user_data, headers=self.headers
        )
        return response

    @allure.step("API: Вход пользователя")
    def login_user(self, email, password):
        # Вход пользователя и сохранение токенов
        login_data = {"email": email, "password": password}
        response = requests.post(
            API_ENDPOINTS["login"], json=login_data, headers=self.headers
        )
        if response.status_code == 200:
            response_data = response.json()
            self.access_token = response_data.get("accessToken")
            self.refresh_token = response_data.get("refreshToken")
            # Обновление заголовков для аутентифицированных запросов
            if self.access_token:
                self.headers["Authorization"] = self.access_token
        return response

    @allure.step("API: Получение информации о пользователе")
    def get_user_info(self):
        # Получение информации о текущем пользователе
        if not self.access_token:
            raise Exception("Пользователь не аутентифицирован")

        response = requests.get(API_ENDPOINTS["user"], headers=self.headers)
        return response

    @allure.step("API: Обновление информации пользователя")
    def update_user_info(self, user_data):
        # Обновление информации пользователя
        if not self.access_token:
            raise Exception("Пользователь не аутентифицирован")

        response = requests.patch(
            API_ENDPOINTS["user"], json=user_data, headers=self.headers
        )
        return response

    @allure.step("API: Выход пользователя")
    def logout_user(self):
        # Выход текущего пользователя
        if not self.refresh_token:
            raise Exception("Пользователь не аутентифицирован")

        logout_data = {"token": self.refresh_token}
        response = requests.post(
            API_ENDPOINTS["logout"], json=logout_data, headers=self.headers
        )

        # Очистка токенов
        self.access_token = None
        self.refresh_token = None
        if "Authorization" in self.headers:
            del self.headers["Authorization"]

        return response

    @allure.step("API: Удаление пользователя")
    def delete_user(self):
        # Удаление текущего аккаунта пользователя
        if not self.access_token:
            raise Exception("Пользователь не аутентифицирован")

        response = requests.delete(API_ENDPOINTS["user"], headers=self.headers)

        # Очистка токенов после удаления
        self.access_token = None
        self.refresh_token = None
        if "Authorization" in self.headers:
            del self.headers["Authorization"]

        return response

    @allure.step("API: Генерация тестовых данных пользователя")
    def generate_test_user(self, email_suffix="test"):
        # Генерация уникальных тестовых данных пользователя
        import uuid

        unique_id = str(uuid.uuid4())[:8]

        from diplom_3.config import TEST_DATA

        return {
            "email": f"{email_suffix}_{unique_id}@{TEST_DATA['email_domain']}",
            "password": TEST_USER["password"],
            "name": f"Test User {unique_id}",
        }

    def is_authenticated(self):
        # Проверка аутентификации пользователя
        return self.access_token is not None