from selenium.webdriver.common.by import By


class PersonalAccountLocators:
    # "Profile" link in personal account
    PROFILE_LINK = (By.XPATH, "//a[@href = '/account/profile']")
    SIGN_OUT_LINK_IN_PROFILE = (By.XPATH, "//button[text() = 'Выход']")
    ORDER_HISTORY = By.XPATH, "//a[text() = 'История заказов']"
    ORDER = By.XPATH, "//a[@class = 'OrderHistory_link__1iNby']"
