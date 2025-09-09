from selenium.webdriver.common.by import By


class LoginPageLocators:
    ENTER_TEXT = (By.XPATH, "//h2[text() = 'Вход']")
    INPUT_EMAIL_AUTH = (By.XPATH, "//input[@name='name']")
    INPUT_PASSWORD_AUTH = (By.XPATH, "//input[@name='Пароль']")
    ENTER_BUTTON = (By.XPATH, ".//button[text()= 'Войти']")
    ENTER_LINK = (By.XPATH, "//a[@href = '/login']")
    FORGET_PASSWORD_LINK = (By.LINK_TEXT, "Восстановить пароль")
