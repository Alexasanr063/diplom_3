import allure
from diplom_3.locators.password_recovery_locators import PasswordResetLocators
from diplom_3.locators.login_locators import AuthFormLocators
from diplom_3.pages.base_page import BasePage


class RestorePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.login_locators = AuthFormLocators()
        self.restore_page_locators = PasswordResetLocators()

    @allure.step("Клик по ссылке восстановления пароля на странице авторизации")
    def click_on_restore_link(self):
        self.click_on_element(self.login_locators.FORGET_PASSWORD_LINK)

    @allure.step("Отображение кнопки восстановления пароля")
    def restore_button_is_visible(self):
        self.wait()
        return self.visibility_of_element(
            self.restore_page_locators.RESET_PASSWORD_BUTTON
        )

    @allure.step("Заполнение поля email")
    def fill_email_field(self):
        self.fill_input(self.restore_page_locators.EMAIL_INPUT_FIELD, "123@yopmail.com")

    @allure.step("Клик по кнопке восстановления пароля")
    def click_on_restore_button(self):
        self.click_on_element(self.restore_page_locators.RESET_PASSWORD_BUTTON)

    @allure.step("Видимость кнопки переключения видимости пароля")
    def eye_button_is_visible(self):
        return self.visibility_of_element(self.restore_page_locators.EYE_BUTTON)

    @allure.step("Ожидание видимости кнопки переключения видимости пароля")
    def wait_visibility_of_eye_button(self):
        self.wait_visibility_of_element(self.restore_page_locators.EYE_BUTTON)

    @allure.step("Клик по полю ввода пароля")
    def click_password_field(self):
        self.click_on_element(self.restore_page_locators.PASSWORD_FIELD)

    @allure.step("Активность поля ввода пароля")
    def field_is_active(self):
        return self.visibility_of_element(
            self.restore_page_locators.ACTIVE_PASSWORD_INPUT
        )