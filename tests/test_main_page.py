import allure
from diplom_3.pages.main_page import MainPage
from diplom_3.tests.conftest import driver_signed_in


@allure.feature("Главная страница")
class TestMainPageFunctionality:
    @allure.description("Переход по клику на 'Конструктор'")
    def test_navigate_to_constructor(self, driver):
        main_page = MainPage(driver)
        main_page.click_in_constructor()
        assert main_page.buns_link_is_visible()

    @allure.description("Переход по клику на 'Лента заказов'")
    def test_navigate_to_order_feed(self, driver):
        main_page = MainPage(driver)
        main_page.click_in_order_feed()
        main_page.wait_for_order_feed_header()
        assert main_page.order_feed_header_is_visible()

    @allure.description("Открытие модального окна с деталями ингредиента")
    def test_ingredient_details_modal(self, driver):
        main_page = MainPage(driver)
        main_page.click_in_constructor()
        main_page.wait_for_bun()
        main_page.click_on_crater_bun()
        main_page.wait_for_modal_window()
        assert main_page.close_modal_window_button_is_visible()

    @allure.description("Закрытие модального окна по клику на кнопку")
    def test_close_ingredient_modal(self, driver):
        main_page = MainPage(driver)
        main_page.click_in_constructor()
        main_page.wait_for_bun()
        main_page.click_on_crater_bun()
        main_page.wait_for_modal_window()
        main_page.close_modal_window()
        assert main_page.buns_link_is_visible()

    @allure.description("Увеличение счетчика при добавлении ингредиента")
    def test_ingredient_counter_increase(self, driver):
        main_page = MainPage(driver)
        main_page.click_in_constructor()
        main_page.wait_for_bun()
        main_page.drag_and_drop_bun()
        assert main_page.bun_counter_is_visible()

    @allure.description("Создание заказа авторизованным пользователем")
    def test_authorized_user_order_placement(self, driver_signed_in):
        main_page = MainPage(driver_signed_in)
        main_page.wait_for_bun()
        main_page.drag_and_drop_bun()
        main_page.make_order()
        main_page.wait_for_made_order_modal_window()
        assert main_page.order_id_is_visible()