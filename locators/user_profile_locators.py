from selenium.webdriver.common.by import By


class PasswordRecoveryLocators:
    """Локаторы для страницы восстановления пароля Burger Palace"""

    # Основные элементы
    RECOVERY_PAGE_TITLE = (By.XPATH, "//h2[text()='Восстановление пароля']")
    EMAIL_INPUT_FIELD = (By.XPATH, "//input[@name='email' and @type='email']")
    RECOVER_PASSWORD_BUTTON = (By.XPATH, "//button[contains(text(), 'Восстановить')]")
    RETURN_TO_LOGIN_LINK = (By.XPATH, "//a[contains(text(), 'Войти')]")

    # Визуальные элементы
    PASSWORD_VISIBILITY_TOGGLE = (
        By.XPATH,
        '//div[contains(@class,"input__icon-action")]//*[local-name()="svg"]'
    )
    ACTIVE_PASSWORD_FIELD = (
        By.XPATH,
        '//div[contains(@class,"input_status_active") and contains(@class,"input_type_password")]'
    )
    PASSWORD_FIELD_CONTAINER = (
        By.XPATH,
        '//div[contains(@class,"input_type_password") and contains(@class,"input_size_default")]'
    )

    # Сообщения и статусы
    RECOVERY_SUCCESS_MSG = (By.XPATH, "//div[contains(text(), 'Письмо отправлено')]")
    ERROR_MESSAGE = (By.XPATH, "//p[contains(@class,'input__error')]")
    LOADING_INDICATOR = (By.XPATH, "//div[contains(@class,'loader__container')]")

    # Дополнительные элементы
    EMAIL_INSTRUCTION_TEXT = (By.XPATH, "//p[contains(text(), 'Введите email')]")
    APP_LOGO = (By.XPATH, "//div[contains(@class,'AppHeader_header__logo')]")