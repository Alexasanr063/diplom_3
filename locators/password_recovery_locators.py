from selenium.webdriver.common.by import By


class PasswordResetLocators:
    RESET_PASSWORD_BUTTON = By.XPATH, "//button[text()='Восстановить']"
    EMAIL_INPUT_FIELD = By.XPATH, "//input[@name='name']"
    EYE_BUTTON = (
        By.XPATH,
        '//div[@class="input__icon input__icon-action"]/*[name()="svg"]',
    )
    ACTIVE_PASSWORD_INPUT = By.XPATH, '//div[contains(@class,"input_status_active")]'
    PASSWORD_FIELD = (
        By.XPATH,
        '//div[@class="input pr-6 pl-6 input_type_password input_size_default"]',
    )
