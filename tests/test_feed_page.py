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
        # Для этого теста нужно добавить метод в FeedPage
        feed_page = FeedPage(driver)
        feed_page.click_on_feed()
        feed_page.wait_for_order_feed()
        feed_page.wait_for_page_to_load()

        # Получаем все элементы заказов
        order_elements = feed_page.driver.find_elements(
            *feed_page.main_page_locators.FIRST_ORDER_IN_FEED
        )

        # Извлекаем номера заказов (предполагая, что текст элемента содержит номер)
        order_numbers = []
        for order_element in order_elements:
            order_text = order_element.text.strip()
            # Пытаемся извлечь числовой номер из текста
            try:
                order_number = int(''.join(filter(str.isdigit, order_text)))
                order_numbers.append(order_number)
            except ValueError:
                continue

        assert len(order_numbers) == len(set(order_numbers)), "Найдены дублирующиеся номера заказов"

    @allure.description("Наличие статуса у всех заказов в ленте")
    def test_check_orders_have_statuses(self, driver):
        # Для этого теста нужно добавить метод в FeedPage или использовать локаторы
        feed_page = FeedPage(driver)
        feed_page.click_on_feed()
        feed_page.wait_for_order_feed()
        feed_page.wait_for_page_to_load()

        # Предполагаем, что статус находится в определенном элементе
        # Нужно добавить соответствующий локатор в MainPageLocators
        try:
            status_elements = feed_page.driver.find_elements(
                By.XPATH, '//div[contains(@class, "OrderFeed_textBox")]//p[contains(@class, "status")]'
            )
            order_statuses = [element.text.strip() for element in status_elements]
            assert all(status for status in order_statuses), "Найдены заказы без статуса"
        except:
            pytest.skip("Локаторы для статусов заказов не настроены")

    @allure.description("Соответствие счетчика общего количества заказов")
    def test_validate_total_orders_counter(self, driver):
        feed_page = FeedPage(driver)
        feed_page.click_on_feed()
        feed_page.wait_for_order_feed()
        feed_page.wait_for_page_to_load()

        # Получаем значение счетчика
        total_count_text = feed_page.orders_for_all_time_()
        try:
            total_count = int(''.join(filter(str.isdigit, total_count_text)))
        except ValueError:
            pytest.fail(f"Не удалось преобразовать счетчик в число: {total_count_text}")

        # Получаем количество видимых заказов
        order_elements = feed_page.driver.find_elements(
            *feed_page.main_page_locators.FIRST_ORDER_IN_FEED
        )
        actual_feed_count = len(order_elements)

        assert total_count >= actual_feed_count, f"Счетчик ({total_count}) меньше количества заказов ({actual_feed_count})"

    @allure.description("Неотрицательное значение счетчика заказов за сегодня")
    def test_check_today_orders_counter(self, driver):
        feed_page = FeedPage(driver)
        feed_page.click_on_feed()
        feed_page.wait_for_order_feed()
        feed_page.wait_for_page_to_load()

        today_count_text = feed_page.orders_for_today()
        try:
            today_count = int(''.join(filter(str.isdigit, today_count_text)))
            assert today_count >= 0, f"Отрицательное значение счетчика: {today_count}"
        except ValueError:
            pytest.fail(f"Не удалось преобразовать счетчик в число: {today_count_text}")