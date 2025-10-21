import allure
import pytest
from diplom_3.pages.order_feed_page import FeedPage
from selenium.webdriver.common.by import By
from diplom_3.tests.conftest import driver_signed_in
from time import sleep


@allure.feature("Лента заказов")
class TestOrderFeed:
    @allure.description("Открытие модального окна с деталями при клике на заказ")
    def test_open_order_details_modal(self, driver):
        feed_page = FeedPage(driver)
        feed_page.click_on_feed()
        feed_page.wait_for_order_feed()
        feed_page.wait_for_page_to_load()
        feed_page.click_on_first_order()
        assert feed_page.order_info_is_displayed()

    @allure.description("Уникальность номеров заказов в ленте")
    def test_verify_unique_order_numbers(self, driver):
        feed_page = FeedPage(driver)
        feed_page.click_on_feed()
        feed_page.wait_for_order_feed()
        feed_page.wait_for_page_to_load()

        order_numbers = feed_page.get_order_numbers_from_feed()
        assert len(order_numbers) == len(set(order_numbers)), "Найдены дублирующиеся номера заказов"

    @allure.description("Наличие статуса у всех заказов в ленте")
    def test_check_orders_have_statuses(self, driver):
        feed_page = FeedPage(driver)
        feed_page.click_on_feed()
        feed_page.wait_for_order_feed()
        feed_page.wait_for_page_to_load()

        order_statuses = feed_page.get_order_statuses()
        assert all(status for status in order_statuses), "Найдены заказы без статуса"

    @allure.description("Соответствие счетчика общего количества заказов")
    def test_validate_total_orders_counter(self, driver):
        feed_page = FeedPage(driver)
        feed_page.click_on_feed()
        feed_page.wait_for_order_feed()
        feed_page.wait_for_page_to_load()

        total_count = feed_page.get_total_orders_count()
        actual_feed_count = feed_page.get_visible_orders_count()

        assert total_count >= actual_feed_count, f"Счетчик ({total_count}) меньше количества заказов ({actual_feed_count})"

    @allure.description("Неотрицательное значение счетчика заказов за сегодня")
    def test_check_today_orders_counter(self, driver):
        feed_page = FeedPage(driver)
        feed_page.click_on_feed()
        feed_page.wait_for_order_feed()
        feed_page.wait_for_page_to_load()

        today_count = feed_page.get_today_orders_count()
        assert today_count >= 0, f"Отрицательное значение счетчика: {today_count}"
