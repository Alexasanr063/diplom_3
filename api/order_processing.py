import requests
import allure
import uuid
from diplom_3.config import API_ENDPOINTS, TEST_USER, MESSAGES


class BurgerUserAPI:
    """API клиент для управления пользователями Stellar Burgers"""

    def __init__(self):
        self.api_base = API_ENDPOINTS["register"].replace("/auth/register", "")
        self.request_headers = {
            "Content-Type": "application/json",
            "X-Client-Version": "stellar-burgers-app-2.1.0"
        }
        self.auth_token = None
        self.refresh_key = None
        self.current_user = None

    @allure.step("API: Зарегистрировать нового пользователя")
    def register_new_user(self, user_info):
        """Регистрация нового пользователя в системе"""
        registration_payload = {
            "email": user_info["email"],
            "password": user_info["password"],
            "name": user_info["name"]
        }

        try:
            response = requests.post(
                API_ENDPOINTS["register"],
                json=registration_payload,
                headers=self.request_headers,
                timeout=10
            )

            if response.status_code == 200:
                self._process_auth_response(response.json())

            return response

        except requests.exceptions.RequestException as e:
            allure.attach(f"Ошибка регистрации: {str(e)}", name="Registration Error")
            raise

    @allure.step("API: Авторизовать пользователя")
    def authenticate_user(self, email, password):
        """Аутентификация пользователя в системе"""
        auth_credentials = {
            "email": email,
            "password": password
        }

        try:
            response = requests.post(
                API_ENDPOINTS["login"],
                json=auth_credentials,
                headers=self.request_headers,
                timeout=8
            )

            if response.status_code == 200:
                self._process_auth_response(response.json())

            return response

        except requests.exceptions.Timeout:
            allure.attach("Таймаут при авторизации", name="Auth Timeout")
            raise Exception(MESSAGES["authorization_required"])

    @allure.step("API: Получить информацию о пользователе")
    def fetch_user_profile(self):
        """Получить профиль текущего пользователя"""
        if not self.auth_token:
            raise Exception(MESSAGES["authorization_required"])

        try:
            auth_headers = {**self.request_headers, "Authorization": f"Bearer {self.auth_token}"}
            response = requests.get(
                API_ENDPOINTS["user"],
                headers=auth_headers,
                timeout=10
            )
            return response

        except requests.exceptions.RequestException as e:
            allure.attach(f"Ошибка получения профиля: {str(e)}", name="Profile Error")
            raise

    @allure.step("API: Обновить информацию пользователя")
    def update_user_profile(self, updated_info):
        """Обновить данные профиля пользователя"""
        if not self.auth_token:
            raise Exception(MESSAGES["authorization_required"])

        try:
            auth_headers = {**self.request_headers, "Authorization": f"Bearer {self.auth_token}"}
            response = requests.patch(
                API_ENDPOINTS["user"],
                json=updated_info,
                headers=auth_headers,
                timeout=12
            )
            return response

        except requests.exceptions.RequestException as e:
            allure.attach(f"Ошибка обновления профиля: {str(e)}", name="Update Error")
            raise

    @allure.step("API: Выйти из системы")
    def user_logout(self):
        """Завершение сессии пользователя"""
        if not self.refresh_key:
            raise Exception("Нет активной сессии для выхода")

        logout_data = {"token": self.refresh_key}

        try:
            response = requests.post(
                API_ENDPOINTS["logout"],
                json=logout_data,
                headers=self.request_headers,
                timeout=5
            )

            self._clear_auth_data()
            return response

        except requests.exceptions.RequestException as e:
            allure.attach(f"Ошибка выхода: {str(e)}", name="Logout Error")
            raise

    @allure.step("API: Удалить аккаунт пользователя")
    def remove_user_account(self):
        """Удаление аккаунта пользователя"""
        if not self.auth_token:
            raise Exception(MESSAGES["authorization_required"])

        try:
            auth_headers = {**self.request_headers, "Authorization": f"Bearer {self.auth_token}"}
            response = requests.delete(
                API_ENDPOINTS["user"],
                headers=auth_headers,
                timeout=15
            )

            self._clear_auth_data()
            return response

        except requests.exceptions.RequestException as e:
            allure.attach(f"Ошибка удаления аккаунта: {str(e)}", name="Deletion Error")
            raise

    @allure.step("API: Сгенерировать тестовые данные пользователя")
    def generate_test_user_data(self, prefix="test_user"):
        """Генерация уникальных тестовых данных пользователя"""
        unique_id = str(uuid.uuid4())[:8]

        return {
            "email": f"{prefix}_{unique_id}@{TEST_USER['email'].split('@')[1]}",
            "password": TEST_USER["password"],
            "name": f"Test User {unique_id}",
        }

    @allure.step("API: Проверить статус аутентификации")
    def is_user_authenticated(self):
        """Проверить, аутентифицирован ли пользователь"""
        return self.auth_token is not None

    def _process_auth_response(self, response_data):
        """Обработка ответа аутентификации"""
        if response_data.get("success"):
            self.auth_token = response_data.get("accessToken")
            self.refresh_key = response_data.get("refreshToken")
            self.current_user = response_data.get("user")

    def _clear_auth_data(self):
        """Очистка данных аутентификации"""
        self.auth_token = None
        self.refresh_key = None
        self.current_user = None

    @allure.step("API: Обновить токен доступа")
    def refresh_auth_token(self):
        """Обновление токена доступа"""
        if not self.refresh_key:
            raise Exception("Нет refresh token для обновления")

        refresh_data = {"token": self.refresh_key}

        try:
            response = requests.post(
                API_ENDPOINTS["token"],
                json=refresh_data,
                headers=self.request_headers,
                timeout=8
            )

            if response.status_code == 200:
                self._process_auth_response(response.json())

            return response

        except requests.exceptions.RequestException as e:
            allure.attach(f"Ошибка обновления токена: {str(e)}", name="Token Refresh Error")
            raise