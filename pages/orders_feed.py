from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from diplom_3.locators.constructor_locators import ConstructorLocators
from diplom_3.pages.core_page import BurgerBasePage
import allure


class OrdersFeedPage(BurgerBasePage):
    """Страница ленты заказов Burger Palace"""

    def __init__(self, driver):
        super().__init__(driver)
        self.locators = ConstructorLocators()

    @allure.step("Ожидание загрузки страницы ленты заказов")
    def wait_for_feed_page_loaded(self):
        """Ожидать полной загрузки страницы ленты заказов"""
        self.wait_for_element_visible(self.locators.ORDER_FEED_TITLE)
        self.wait_for_element_visible(self.locators.ORDER_ITEMS_LIST)

    @allure.step("Открытие ленты заказов")
    def open_orders_feed(self):
        """Открыть раздел ленты заказов"""
        self.click_element(self.locators.ORDER_FEED_TAB)
        self.wait_for_feed_page_loaded()

    @allure.step("Клик по первому заказу в ленте")
    def click_first_order(self):
        """Кликнуть по первому заказу в ленте для просмотра деталей"""
        self.click_element(self.locators.FIRST_ORDER_ITEM)
        self.wait_for_modal_opened()

    @allure.step("Ожидание открытия модального окна")
    def wait_for_modal_opened(self):
        """Ожидать открытия модального окна с деталями заказа"""
        self.wait_for_element_visible(self.locators.ORDER_MODAL)

    @allure.step("Проверка отображения информации о заказе")
    def is_order_info_displayed(self):
        """Проверить отображается ли информация о заказе"""
        return self.is_element_visible(self.locators.ORDER_MODAL)

    @allure.step("Скролл к моим заказам")
    def scroll_to_my_orders(self):
        """Проскроллить к разделу с моими заказами"""
        self.scroll_to_element(self.locators.ORDER_ITEMS_LIST)

    @allure.step("Проверка видимости моего заказа")
    def is_my_order_visible(self):
        """Проверить виден ли мой заказ в ленте"""
        return self.is_element_visible(self.locators.FIRST_ORDER_ITEM)

    @allure.step("Получение количества заказов за все время")
    def get_total_orders_count(self):
        """Получить количество выполненных заказов за все время"""
        return self.get_element_text(self.locators.ORDERS_TOTAL)

    @allure.step("Получение количества заказов за сегодня")
    def get_today_orders_count(self):
        """Получить количество выполненных заказов за сегодня"""
        return self.get_element_text(self.locators.ORDERS_TODAY)

    @allure.step("Закрытие модального окна")
    def close_order_modal(self):
        """Закрыть модальное окно с деталями заказа"""
        try:
            self.click_element(self.locators.MODAL_CLOSE_BUTTON)
            self.wait_for_element_invisible(self.locators.ORDER_MODAL)
        except Exception:
            self.press_escape()

    @allure.step("Получение номера заказа в процессе")
    def get_order_in_progress_number(self):
        """Получить номер заказа в разделе 'В работе'"""
        if self.is_element_visible(self.locators.ORDERS_IN_PROGRESS):
            return self.get_element_text(self.locators.ORDERS_IN_PROGRESS)
        return None

    @allure.step("Ожидание появления заказа в ленте")
    def wait_for_order_in_feed(self, timeout=30):
        """Ожидать появления любого заказа в ленте"""
        self.wait_for_element_visible(self.locators.ORDER_ITEMS_LIST, timeout)

    @allure.step("Ожидание конкретного номера заказа")
    def wait_for_specific_order_number(self, order_number, timeout=45):
        """Ожидать появления конкретного номера заказа в ленте"""

        def order_number_appears(driver):
            try:
                # Проверяем различные возможные места появления номера заказа
                possible_elements = driver.find_elements(
                    *self.locators.ORDERS_IN_PROGRESS
                )

                for element in possible_elements:
                    element_text = element.text.strip()
                    if str(order_number) in element_text:
                        return True

                # Дополнительная проверка по всем элементам заказов
                order_elements = driver.find_elements(*self.locators.ORDER_ITEMS)
                for order_element in order_elements:
                    order_text = order_element.text
                    if str(order_number) in order_text:
                        return True

                return False
            except Exception:
                return False

        return WebDriverWait(self.driver, timeout).until(order_number_appears)

    @allure.step("Проверка активности раздела ленты заказов")
    def is_feed_tab_active(self):
        """Проверить активен ли таб ленты заказов"""
        element = self.find_element(self.locators.ORDER_FEED_TAB)
        return "tab_tab_type_current__" in element.get_attribute("class")

    @allure.step("Обновление ленты заказов")
    def refresh_orders_feed(self):
        """Обновить ленту заказов"""
        self.refresh_page()
        self.wait_for_feed_page_loaded()