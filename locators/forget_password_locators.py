from selenium.webdriver.common.by import By


class ForgetPasswordLocators:
    RESTORE_PASSWORD_BUTTON = By.XPATH, "//button[text()='Восстановить']"
    INPUT_EMAIL = By.XPATH, "//input[@name='name']"
    EYE_BUTTON = (
        By.XPATH,
        '//div[@class="input__icon input__icon-action"]/*[name()="svg"]',
    )
    ACTIVE_PASSWORD_FIELD = By.XPATH, '//div[contains(@class,"input_status_active")]'
    PASSWORD_FIELD = (
        By.XPATH,
        '//div[@class="input pr-6 pl-6 input_type_password input_size_default"]',
    )
