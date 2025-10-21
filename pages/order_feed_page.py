import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

from diplom_3.locators.main_page_locators import BurgerAppLocators
from diplom_3.pages.base_page import BasePage
import allure


class FeedPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.main_page_locators = BurgerAppLocators()

    @allure.step("Ожидание полной загрузки страницы ленты")
    def wait_for_page_to_load(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.main_page_locators.ORDER_ID)
        )

    @allure.step("Клик по кнопке ленты заказов")
    def click_on_feed(self):
        self.click_on_element(self.main_page_locators.ORDERS_FEED_LINK)

    @allure.step("Клик по первому заказу в ленте")
    def click_on_first_order(self):
        self.click_on_element(self.main_page_locators.FIRST_ORDER_IN_FEED)
        self.wait_visibility_of_element(self.main_page_locators.MODAL_OPENED)

    @allure.step("Отображение номера заказа")
    def order_info_is_displayed(self):
        return self.visibility_of_element(self.main_page_locators.ORDER_DETAILS_MODAL)

    @allure.step("Ожидание загрузки ленты заказов")
    def wait_for_order_feed(self):
        self.wait_visibility_of_element(self.main_page_locators.FIRST_ORDER_IN_FEED)

    @allure.step("Получение номеров заказов из ленты")
    def get_order_numbers_from_feed(self):
        order_elements = self.driver.find_elements(
            *self.main_page_locators.FIRST_ORDER_IN_FEED
        )

        order_numbers = []
        for order_element in order_elements:
            order_text = order_element.text.strip()
            try:
                order_number = int(''.join(filter(str.isdigit, order_text)))
                order_numbers.append(order_number)
            except ValueError:
                continue
        return order_numbers

    @allure.step("Получение статусов заказов")
    def get_order_statuses(self):
        try:
            status_elements = self.driver.find_elements(
                By.XPATH, '//div[contains(@class, "OrderFeed_textBox")]//p[contains(@class, "status")]'
            )
            return [element.text.strip() for element in status_elements]
        except:
            return []

    @allure.step("Получение общего количества заказов")
    def get_total_orders_count(self):
        total_count_text = self.orders_for_all_time()
        try:
            return int(''.join(filter(str.isdigit, total_count_text)))
        except ValueError:
            pytest.fail(f"Не удалось преобразовать счетчик в число: {total_count_text}")

    @allure.step("Получение количества заказов за сегодня")
    def get_today_orders_count(self):
        today_count_text = self.orders_for_today()
        try:
            return int(''.join(filter(str.isdigit, today_count_text)))
        except ValueError:
            pytest.fail(f"Не удалось преобразовать счетчик в число: {today_count_text}")

    @allure.step("Получение количества видимых заказов")
    def get_visible_orders_count(self):
        order_elements = self.driver.find_elements(
            *self.main_page_locators.FIRST_ORDER_IN_FEED
        )
        return len(order_elements)

    @allure.step("Все заказы за все время")
    def orders_for_all_time(self):
        return self.text_of_element(self.main_page_locators.ORDERS_FOR_ALL_TIME)

    @allure.step("Все заказы за сегодня")
    def orders_for_today(self):
        return self.text_of_element(self.main_page_locators.ORDERS_FOR_TODAY)

    # Остальные методы остаются без изменений
    @allure.step("Прокрутка к заказу")
    def scroll_to_order(self):
        self.scroll_to_element(self.main_page_locators.MY_ORDER_IN_ORDER_FEED)

    @allure.step("Видимость заказа")
    def my_order_is_visible(self):
        return self.visibility_of_element(
            self.main_page_locators.MY_ORDER_IN_ORDER_FEED
        )

    @allure.step("Перемещение элемента в корзину")
    def drag_and_drop_bun(self):
        self.move_element(
            self.main_page_locators.CRATER_BUN,
            self.main_page_locators.BURGER_INGREDIENTS,
        )

    @allure.step("Клик по кнопке оформления заказа")
    def make_order(self):
        self.click_on_element(self.main_page_locators.PLACE_ORDER_BUTTON)

    @allure.step("Закрытие модального окна")
    def close_modal_window(self):
        try:
            self.wait_visibility_of_element(
                self.main_page_locators.MODAL_OPENED, timeout=5
            )
            close_button = self.driver.find_element(
                *self.main_page_locators.CLOSE_MODAL_WINDOW_BUTTON
            )
            self.driver.execute_script("arguments[0].click();", close_button)
        except Exception:
            from selenium.webdriver.common.keys import Keys
            self.driver.find_element("tag name", "body").send_keys(Keys.ESCAPE)

    @allure.step("Клик по кнопке конструктора на текущей странице")
    def click_on_constructor(self):
        self.click_on_element(self.main_page_locators.CONSTRUCTOR_LINK)

    @allure.step("Ожидание закрытия модального окна")
    def wait_for_modal_window_to_be_closed(self):
        self.wait_order_modal_window_closed(
            self.main_page_locators.EXTRA_ORDER_MODAL_WINDOW
        )

    @allure.step("Номер заказа в ленте заказов")
    def get_order_in_feed(self):
        return self.text_of_element(self.main_page_locators.ORDER_IN_PROCESS_IN_FEED)

    @allure.step("Номер нового заказа")
    def get_order_in_main_page(self):
        return self.text_of_element(self.main_page_locators.ORDER_IN_MODAL_WINDOW)

    @allure.step("Видимость заказа")
    def wait_for_order_number(self):
        return self.wait_visibility_of_element(
            self.main_page_locators.ORDER_IN_PROCESS_IN_FEED
        )

    @allure.step("Ожидание увеличения счетчика")
    def wait_for_counter_increase(self, locator, old_value, timeout=30):
        def counter_increased(driver):
            try:
                current_text = driver.find_element(*locator).text
                current_value = int(current_text)
                return current_value > old_value
            except (ValueError, TypeError):
                return False

        return WebDriverWait(self.driver, timeout).until(counter_increased)

    @allure.step("Ожидание конкретного номера заказа в ленте")
    def wait_for_specific_order_in_feed(self, expected_order_number, timeout=30):
        def order_number_appears(driver):
            try:
                possible_locators = [
                    self.main_page_locators.ORDER_IN_PROCESS_IN_FEED,
                    (By.XPATH, '//div[contains(@class, "OrderFeed_textBox")]/ul/li[contains(@class, "digits")]'),
                    (By.XPATH, '//li[contains(@class, "text_type_digits-default")]'),
                    (By.XPATH, f'//*[text()="{expected_order_number}"]'),
                    (By.XPATH, f'//*[contains(text(), "{expected_order_number}")]'),
                ]

                for locator in possible_locators:
                    try:
                        elements = driver.find_elements(*locator)
                        for element in elements:
                            element_text = element.text.strip()
                            if str(expected_order_number) in element_text:
                                return True
                            try:
                                if int(element_text) == expected_order_number:
                                    return True
                            except (ValueError, TypeError):
                                continue
                    except Exception:
                        continue
                return False
            except Exception:
                return False

        return WebDriverWait(self.driver, timeout).until(order_number_appears)
