import allure
from diplom_3.pages.personal_account_page import PersonalAccountPage
from diplom_3.tests.conftest import driver_signed_in


@allure.feature("Личный кабинет")
class TestPersonalAccount:
    @allure.description("Переход в личный кабинет по клику")
    def test_personal_account_navigation(self, driver_signed_in):
        account_page = PersonalAccountPage(driver_signed_in)
        account_page.click_on_personal_account_button()
        account_page.wait_for_log_out_button()
        assert account_page.in_personal_account_page()

    @allure.description("Отображение раздела 'История заказов'")
    def test_order_history_section(self, driver_signed_in):
        account_page = PersonalAccountPage(driver_signed_in)
        account_page.click_on_personal_account_button()
        account_page.wait_for_log_out_button()
        account_page.click_on_order_history_button()
        account_page.wait_for_order_history_is_displayed()
        assert account_page.order_history_is_displayed()

    @allure.description("Выход из учетной записи")
    def test_user_logout(self, driver_signed_in):
        account_page = PersonalAccountPage(driver_signed_in)
        account_page.click_on_personal_account_button()
        account_page.wait_for_log_out_button()
        account_page.click_log_out_button()
        account_page.wait_for_log_in_button_is_displayed()
        assert account_page.login_button_is_displayed()