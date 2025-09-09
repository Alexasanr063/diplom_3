from selenium.webdriver.common.by import By


class UserProfileLocators:
    # "Profile" link in personal account
    PROFILE_SECTION_LINK = (By.XPATH, "//a[@href = '/account/profile']")
    LOGOUT_BUTTON = (By.XPATH, "//button[text() = 'Выход']")
    ORDER_HISTORY_LINK = By.XPATH, "//a[text() = 'История заказов']"
    ORDER = By.XPATH, "//a[@class = 'OrderHistory_link__1iNby']"
