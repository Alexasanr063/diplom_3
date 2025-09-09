import allure

from diplom_3.locators.login_locators import AuthFormLocators
from diplom_3.locators.profile_locators import UserProfileLocators
from diplom_3.locators.main_page_locators import BurgerAppLocators
from diplom_3.pages.base_page import BasePage


class PersonalAccountPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.main_page_locators = BurgerAppLocators()
        self.personal_account_locators = UserProfileLocators()
        self.login_page_locators = AuthFormLocators()

    @allure.step("Клик по кнопке личного кабинета на главной странице")
    def click_on_personal_account_button(self):
        self.click_on_element(self.main_page_locators.ACCOUNT_LINK)

    @allure.step("Видимость кнопки выхода")
    def in_personal_account_page(self):
        return self.visibility_of_element(
            self.personal_account_locators.LOGOUT_BUTTON
        )

    @allure.step("Ожидание кнопки выхода")
    def wait_for_log_out_button(self):
        self.wait_visibility_of_element(
            self.personal_account_locators.LOGOUT_BUTTON
        )

    @allure.step("Клик по истории заказов")
    def click_on_order_history_button(self):
        self.click_on_element(self.personal_account_locators.ORDER_HISTORY_LINK)

    @allure.step("Ожидание появления заказа")
    def wait_for_order_history_is_displayed(self):
        self.wait_visibility_of_element(self.personal_account_locators.ORDER)

    @allure.step("Видимость заказа")
    def order_history_is_displayed(self):
        return self.visibility_of_element(self.personal_account_locators.ORDER)

    @allure.step("Клик по кнопке выхода")
    def click_log_out_button(self):
        self.click_on_element(self.personal_account_locators.LOGOUT_BUTTON)

    @allure.step("Ожидание видимости кнопки входа")
    def wait_for_log_in_button_is_displayed(self):
        self.wait_visibility_of_element(self.login_page_locators.SIGN_IN_BUTTON)

    @allure.step("Видимость кнопки входа")
    def login_button_is_displayed(self):
        return self.visibility_of_element(self.login_page_locators.SIGN_IN_BUTTON)