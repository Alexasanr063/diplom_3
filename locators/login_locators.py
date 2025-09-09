from selenium.webdriver.common.by import By


class AuthFormLocators:
    LOGIN_TITLE = (By.XPATH, "//h2[text() = 'Вход']")
    EMAIL_FIELD = (By.XPATH, "//input[@name='name']")
    INPUT_PASSWORD_AUTH = (By.XPATH, "//input[@name='Пароль']")
    SIGN_IN_BUTTON = (By.XPATH, ".//button[text()= 'Войти']")
    ENTER_LINK = (By.XPATH, "//a[@href = '/login']")
    FORGET_PASSWORD_LINK = (By.LINK_TEXT, "Восстановить пароль")
