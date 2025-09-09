import allure
from diplom_3.locators.authentication_locators import AuthenticationLocators
from diplom_3.locators.recovery_locators import RecoveryLocators
from diplom_3.pages.core_page import BurgerBasePage


class PasswordRecoveryPage(BurgerBasePage):
    """Страница восстановления пароля Burger Palace"""

    def __init__(self, driver):
        super().__init__(driver)
        self.auth_locators = AuthenticationLocators()
        self.recovery_locators = RecoveryLocators()

    @allure.step("Открытие страницы восстановления пароля")
    def open_password_recovery(self):
        """Открыть страницу восстановления пароля"""
        self.click_element(self.auth_locators.PASSWORD_RECOVERY_LINK)
        self.wait_for_recovery_page_loaded()

    @allure.step("Ожидание загрузки страницы восстановления")
    def wait_for_recovery_page_loaded(self):
        """Ожидать загрузки страницы восстановления пароля"""
        self.wait_for_element_visible(self.recovery_locators.RECOVERY_FORM_TITLE)

    @allure.step("Заполнение email для восстановления")
    def fill_recovery_email(self, email):
        """Заполнить поле email для восстановления пароля"""
        self.fill_field(self.recovery_locators.EMAIL_INPUT_FIELD, email)

    @allure.step("Отправка запроса на восстановление")
    def submit_recovery_request(self):
        """Отправить запрос на восстановление пароля"""
        self.click_element(self.recovery_locators.RESTORE_PASSWORD_BUTTON)
        self.wait_for_recovery_response()

    @allure.step("Ожидание ответа на запрос восстановления")
    def wait_for_recovery_response(self):
        """Ожидать ответа на запрос восстановления пароля"""
        # Может быть успешное сообщение или ошибка
        try:
            self.wait_for_element_visible(self.recovery_locators.SUCCESS_MESSAGE, timeout=10)
        except:
            # Если нет успешного сообщения, проверяем наличие ошибки
            self.wait_for_element_visible(self.recovery_locators.ERROR_MESSAGE, timeout=5)

    @allure.step("Возврат к странице авторизации")
    def back_to_login(self):
        """Вернуться к странице авторизации"""
        self.click_element(self.recovery_locators.BACK_TO_LOGIN_LINK)
        self.wait_for_element_visible(self.auth_locators.LOGIN_BUTTON)

    @allure.step("Переключение видимости пароля")
    def toggle_password_visibility(self):
        """Переключить видимость пароля"""
        self.click_element(self.recovery_locators.PASSWORD_VISIBILITY_TOGGLE)

    @allure.step("Проверка активности поля пароля")
    def is_password_field_active(self):
        """Проверить активно ли поле пароля"""
        return self.is_element_visible(self.recovery_locators.ACTIVE_PASSWORD_FIELD)

    @allure.step("Проверка успешности отправки запроса")
    def is_recovery_successful(self):
        """Проверить успешно ли отправлен запрос восстановления"""
        return self.is_element_visible(self.recovery_locators.SUCCESS_MESSAGE)

    @allure.step("Получение сообщения об ошибке")
    def get_error_message(self):
        """Получить сообщение об ошибке если есть"""
        if self.is_element_visible(self.recovery_locators.ERROR_MESSAGE):
            return self.get_element_text(self.recovery_locators.ERROR_MESSAGE)
        return None
