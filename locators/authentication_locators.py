from selenium.webdriver.common.by import By


class AuthenticationLocators:
    """Локаторы для страницы авторизации Burger Palace"""

    # Заголовки и тексты
    PAGE_TITLE = (By.XPATH, "//h2[text()='Вход в аккаунт']")
    WELCOME_MESSAGE = (By.XPATH, "//p[contains(text(), 'Добро пожаловать')]")

    # Поля ввода
    EMAIL_INPUT = (By.XPATH, "//input[@name='email' and @type='email']")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='password' and @type='password']")

    # Кнопки
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Войти в систему')]")
    SHOW_PASSWORD_BUTTON = (
        By.XPATH,
        "//div[contains(@class,'input__icon-action')]//*[local-name()='svg']"
    )

    # Ссылки и переходы
    REGISTER_LINK = (By.XPATH, "//a[contains(@href, '/register') and contains(text(), 'Регистрация')]")
    PASSWORD_RECOVERY_LINK = (
        By.XPATH,
        "//a[contains(@href, '/forgot-password') and contains(text(), 'Забыли пароль?')]"
    )

    # Состояния формы
    ACTIVE_EMAIL_FIELD = (By.XPATH, "//div[contains(@class,'input_status_active')]//input[@name='email']")
    ERROR_MESSAGE = (By.XPATH, "//p[contains(@class,'input__error-text')]")
    SUCCESS_LOGIN_INDICATOR = (By.XPATH, "//div[contains(text(), 'Успешный вход')]")

    # Дополнительные элементы
    REMEMBER_ME_CHECKBOX = (By.XPATH, "//input[@type='checkbox' and @name='remember']")
    SOCIAL_LOGIN_BUTTONS = (By.XPATH, "//button[contains(@class,'social-login__button')]")