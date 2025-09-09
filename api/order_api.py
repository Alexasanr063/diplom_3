import requests
import allure
from diplom_3.config import API_ENDPOINTS, TEST_DATA


class OrderAPI:
    # API client for order-related operations

    def __init__(self, access_token=None):
        self.headers = {"Content-Type": "application/json"}
        if access_token:
            self.headers["Authorization"] = access_token

    def set_auth_token(self, access_token):
        # Set authorization token for authenticated requests
        if access_token:
            self.headers["Authorization"] = access_token
        elif "Authorization" in self.headers:
            del self.headers["Authorization"]

    @allure.step("API: Get ingredients")
    def get_ingredients(self):
        # Get all available ingredients
        response = requests.get(API_ENDPOINTS["ingredients"], headers=self.headers)
        return response

    @allure.step("API: Create order")
    def create_order(self, ingredient_ids):
        # Create a new order with the given ingredient IDs
        order_data = {"ingredients": ingredient_ids}
        response = requests.post(
            API_ENDPOINTS["orders"], json=order_data, headers=self.headers
        )
        return response

    @allure.step("API: Get user orders")
    def get_user_orders(self):
        # Get orders for the authenticated user
        response = requests.get(API_ENDPOINTS["orders"], headers=self.headers)
        return response

    @allure.step("API: Get order by number")
    def get_order_by_number(self, order_number):
        # Get order details by order number
        response = requests.get(
            f"{API_ENDPOINTS['orders']}/{order_number}", headers=self.headers
        )
        return response

    @allure.step("API: Get all orders (feed)")
    def get_all_orders(self):
        # Get all orders from the public feed
        response = requests.get(API_ENDPOINTS["orders_all"], headers=self.headers)
        return response

    @allure.step("API: Create test order with default ingredients")
    def create_test_order(self):
        # Create a test order with predefined ingredients
        # Use predefined test ingredient IDs from config
        test_ingredients = TEST_DATA["ingredient_ids"]
        return self.create_order(test_ingredients)

    def is_authenticated(self):
        # Check if API client has authentication token
        return "Authorization" in self.headers
