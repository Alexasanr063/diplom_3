import allure
from diplom_3.locators.forget_password_locators import ForgetPasswordLocators
from diplom_3.locators.login_page_locators import LoginPageLocators
from diplom_3.pages.base_page import BasePage


class RestorePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.login_locators = LoginPageLocators()
        self.restore_page_locators = ForgetPasswordLocators()

    @allure.step("Click on password reset link on authorization page")
    def click_on_restore_link(self):
        self.click_on_element(self.login_locators.FORGET_PASSWORD_LINK)

    @allure.step("Reset password button is displayed")
    def restore_button_is_visible(self):
        self.wait()
        return self.visibility_of_element(
            self.restore_page_locators.RESTORE_PASSWORD_BUTTON
        )

    @allure.step("Fill email field")
    def fill_email_field(self):
        self.fill_input(self.restore_page_locators.INPUT_EMAIL, "123@yopmail.com")

    @allure.step("Click on password reset button")
    def click_on_restore_button(self):
        self.click_on_element(self.restore_page_locators.RESTORE_PASSWORD_BUTTON)

    @allure.step("Password visibility toggle button is visible")
    def eye_button_is_visible(self):
        return self.visibility_of_element(self.restore_page_locators.EYE_BUTTON)

    @allure.step("Wait for password visibility toggle button")
    def wait_visibility_of_eye_button(self):
        self.wait_visibility_of_element(self.restore_page_locators.EYE_BUTTON)

    @allure.step("Click on password input field")
    def click_password_field(self):
        self.click_on_element(self.restore_page_locators.PASSWORD_FIELD)

    @allure.step("Password input field is active")
    def field_is_active(self):
        return self.visibility_of_element(
            self.restore_page_locators.ACTIVE_PASSWORD_FIELD
        )
