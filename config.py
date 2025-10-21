# Constants used across the project

# Base URLs
BASE_URL = "https://stellarburgers.nomoreparties.site"
API_URL = f"{BASE_URL}/api"

# locators URLs
PAGE_URLS = {
    "main": BASE_URL,
    "login": f"{BASE_URL}/login",
    "register": f"{BASE_URL}/register",
    "forgot_password": f"{BASE_URL}/forgot-password",
    "reset_password": f"{BASE_URL}/reset-password",
    "profile": f"{BASE_URL}/account/profile",
    "feed": f"{BASE_URL}/feed",
}

# API Endpoints
API_ENDPOINTS = {
    "register": f"{API_URL}/auth/register",
    "login": f"{API_URL}/auth/login",
    "logout": f"{API_URL}/auth/logout",
    "token": f"{API_URL}/auth/token",
    "user": f"{API_URL}/auth/user",
    "orders": f"{API_URL}/orders",
    "orders_all": f"{API_URL}/orders/all",
    "ingredients": f"{API_URL}/ingredients",
    "password_reset": f"{API_URL}/password-reset",
    "password_reset_confirm": f"{API_URL}/password-reset/reset",
}

# Test User Data
TEST_USER = {
    "email": "naty@yopmail.com",
    "password": "password123",
    "name": "Test User",
    "invalid_password": "123",
}

# Test Data
TEST_DATA = {
    "email_domain": "yopmail.com",
    "ingredient_name": "Краторная булка N-200i",
    "sauce_name": "Соус Spicy-X",
    "ingredient_ids": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa6f"],
}

# Expected Messages
MESSAGES = {
    "success": "success",
    "user_exists": "User already exists",
    "fields_required": "Email, password and name are required fields",
    "incorrect_credentials": "email or password are incorrect",
    "logout_success": "Successful logout",
    "password_reset_email_sent": "Reset email sent",
    "password_reset_success": "Password successfully reset",
    "authorization_required": "You should be authorised",
}

# Browser Configuration
BROWSER_CONFIG = {
    "default": "chrome",
    "headless": "--headless",
    "window_size": "--window-size=1920,1080",
}

# Timeout
DEFAULT_TIMEOUT = 10

# Order Status
ORDER_STATUS = {
    "done": "done",
}
