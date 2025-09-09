import requests
import allure
from diplom_3.config import API_ENDPOINTS, TEST_USER, MESSAGES


class UserAPI:
    # API client for user-related operations

    def __init__(self):
        self.base_url = API_ENDPOINTS["register"].replace("/auth/register", "")
        self.headers = {"Content-Type": "application/json"}
        self.access_token = None
        self.refresh_token = None

    @allure.step("API: Register user")
    def register_user(self, user_data):
        # Register a new user
        response = requests.post(
            API_ENDPOINTS["register"], json=user_data, headers=self.headers
        )
        return response

    @allure.step("API: Login user")
    def login_user(self, email, password):
        # Login user and store tokens
        login_data = {"email": email, "password": password}
        response = requests.post(
            API_ENDPOINTS["login"], json=login_data, headers=self.headers
        )
        if response.status_code == 200:
            response_data = response.json()
            self.access_token = response_data.get("accessToken")
            self.refresh_token = response_data.get("refreshToken")
            # Update headers for authenticated requests
            if self.access_token:
                self.headers["Authorization"] = self.access_token
        return response

    @allure.step("API: Get user info")
    def get_user_info(self):
        # Get current user information
        if not self.access_token:
            raise Exception("User not authenticated")

        response = requests.get(API_ENDPOINTS["user"], headers=self.headers)
        return response

    @allure.step("API: Update user info")
    def update_user_info(self, user_data):
        # Update user information
        if not self.access_token:
            raise Exception("User not authenticated")

        response = requests.patch(
            API_ENDPOINTS["user"], json=user_data, headers=self.headers
        )
        return response

    @allure.step("API: Logout user")
    def logout_user(self):
        # Logout current user
        if not self.refresh_token:
            raise Exception("User not authenticated")

        logout_data = {"token": self.refresh_token}
        response = requests.post(
            API_ENDPOINTS["logout"], json=logout_data, headers=self.headers
        )

        # Clear tokens
        self.access_token = None
        self.refresh_token = None
        if "Authorization" in self.headers:
            del self.headers["Authorization"]

        return response

    @allure.step("API: Delete user")
    def delete_user(self):
        # Delete current user account
        if not self.access_token:
            raise Exception("User not authenticated")

        response = requests.delete(API_ENDPOINTS["user"], headers=self.headers)

        # Clear tokens after deletion
        self.access_token = None
        self.refresh_token = None
        if "Authorization" in self.headers:
            del self.headers["Authorization"]

        return response

    @allure.step("API: Generate test user data")
    def generate_test_user(self, email_suffix="test"):
        # Generate unique test user data
        import uuid

        unique_id = str(uuid.uuid4())[:8]

        from diplom_3.config import TEST_DATA

        return {
            "email": f"{email_suffix}_{unique_id}@{TEST_DATA['email_domain']}",
            "password": TEST_USER["password"],
            "name": f"Test User {unique_id}",
        }

    def is_authenticated(self):
        # Check if user is currently authenticated
        return self.access_token is not None
