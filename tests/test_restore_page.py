from diplom_3.pages.password_restore_page import RestorePage
import allure


@allure.feature("Восстановление пароля")
class TestRestorePage:
    @allure.title("Отображение кнопки 'Восстановить' после перехода по ссылке восстановления пароля")
    def test_restore_button_visibility(self, driver):
        restore_page = RestorePage(driver)
        restore_page.click_on_restore_link()
        assert restore_page.restore_button_is_visible()

    @allure.title("Появление формы восстановления пароля после ввода email")
    def test_restore_form_appearance(self, driver):
        restore_page = RestorePage(driver)
        restore_page.click_on_restore_link()
        restore_page.fill_email_field()
        restore_page.click_on_restore_button()
        restore_page.wait_visibility_of_eye_button()
        assert restore_page.eye_button_is_visible()

    @allure.title("Активация поля ввода пароля при клике")
    def test_password_field_activation(self, driver):
        restore_page = RestorePage(driver)
        restore_page.click_on_restore_link()
        restore_page.fill_email_field()
        restore_page.click_on_restore_button()
        restore_page.wait_visibility_of_eye_button()
        restore_page.click_password_field()
        assert restore_page.field_is_active()