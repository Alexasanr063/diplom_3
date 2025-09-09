from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

from diplom_3.locators.main_page_locators import MainPageLocators
from diplom_3.pages.base_page import BasePage
import allure


class FeedPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.main_page_locators = MainPageLocators()

    @allure.step("Wait for feed page fully loaded ")
    def wait_for_page_to_load(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.main_page_locators.ORDER_ID)
        )

    @allure.step("Wait for modal window")
    def wait_for_modal_to_open(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.main_page_locators.MODAL_OPENED)
        )

    @allure.step("Button click feed")
    def click_on_feed(self):
        self.click_on_element(self.main_page_locators.ORDER_FEED_LINK)

    @allure.step("Click first order in feed")
    def click_on_first_order(self):
        self.click_on_element(self.main_page_locators.FIRST_ORDER_IN_FEED)
        self.wait_visibility_of_element(self.main_page_locators.MODAL_OPENED)

    @allure.step("Order number")
    def order_info_is_displayed(self):
        return self.visibility_of_element(self.main_page_locators.ORDER_INFO)

    @allure.step("Wait for order feed")
    def wait_for_order_feed(self):
        self.wait_visibility_of_element(self.main_page_locators.FIRST_ORDER_IN_FEED)

    @allure.step("Order scroll to")
    def scroll_to_order(self):
        self.scroll_to_element(self.main_page_locators.MY_ORDER_IN_ORDER_FEED)

    @allure.step("Order visible")
    def my_order_is_visible(self):
        return self.visibility_of_element(
            self.main_page_locators.MY_ORDER_IN_ORDER_FEED
        )

    @allure.step("All orders for all time")
    def orders_for_all_time_(self):
        return self.text_of_element(self.main_page_locators.ORDERS_FOR_ALL_TIME)

    @allure.step("All orders for today")
    def orders_for_today(self):
        return self.text_of_element(self.main_page_locators.ORDERS_FOR_TODAY)

    @allure.step("Element move to bucket")
    def drag_and_drop_bun(self):
        self.move_element(
            self.main_page_locators.CRATER_BUN,
            self.main_page_locators.BURGER_INGREDIENTS,
        )

    @allure.step("Button click place order")
    def make_order(self):
        self.click_on_element(self.main_page_locators.BUTTON_MAKE_ORDER)

    @allure.step("Modal window close")
    def close_modal_window(self):
        # Try clicking the modal overlay first to dismiss it, or use JavaScript click
        try:
            # Wait for the modal to be fully visible
            self.wait_visibility_of_element(
                self.main_page_locators.MODAL_OPENED, timeout=5
            )
            # Use JavaScript to click the close button to avoid overlay issues
            close_button = self.driver.find_element(
                *self.main_page_locators.CLOSE_MODAL_WINDOW_BUTTON
            )
            self.driver.execute_script("arguments[0].click();", close_button)
        except Exception:
            # Fallback: try pressing Escape key
            from selenium.webdriver.common.keys import Keys

            self.driver.find_element("tag name", "body").send_keys(Keys.ESCAPE)

    @allure.step("Button click constructor current page")
    def click_on_constructor(self):
        self.click_on_element(self.main_page_locators.CONSTRUCTOR_LINK)

    @allure.step("Modal window close")
    def wait_for_modal_window_to_be_closed(self):
        self.wait_order_modal_window_closed(
            self.main_page_locators.EXTRA_ORDER_MODAL_WINDOW
        )

    @allure.step("Order number in order feed")
    def get_order_in_feed(self):
        return self.text_of_element(self.main_page_locators.ORDER_IN_PROCESS_IN_FEED)

    @allure.step("Order number new order")
    def get_order_in_main_page(self):
        return self.text_of_element(self.main_page_locators.ORDER_IN_MODAL_WINDOW)

    @allure.step("Order visible")
    def wait_for_order_number(self):
        return self.wait_visibility_of_element(
            self.main_page_locators.ORDER_IN_PROCESS_IN_FEED
        )

    @allure.step("Wait for counter to increase")
    def wait_for_counter_increase(self, locator, old_value, timeout=30):
        # Wait for numerical counter to increase from old_value

        def counter_increased(driver):
            try:
                current_text = driver.find_element(*locator).text
                current_value = int(current_text)
                return current_value > old_value
            except (ValueError, TypeError):
                return False

        return WebDriverWait(self.driver, timeout).until(counter_increased)

    @allure.step("Wait for specific order number in feed")
    def wait_for_specific_order_in_feed(self, expected_order_number, timeout=30):
        # Wait for specific order number to appear in the 'В работе' section or any order section

        def order_number_appears(driver):
            try:
                # Try multiple possible locators for orders in progress
                possible_locators = [
                    self.main_page_locators.ORDER_IN_PROCESS_IN_FEED,
                    (
                        By.XPATH,
                        '//div[contains(@class, "OrderFeed_textBox")]/ul/li[contains(@class, "digits")]',
                    ),
                    (By.XPATH, '//li[contains(@class, "text_type_digits-default")]'),
                    (By.XPATH, f'//*[text()="{expected_order_number}"]'),
                    (By.XPATH, f'//*[contains(text(), "{expected_order_number}")]'),
                ]

                for locator in possible_locators:
                    try:
                        elements = driver.find_elements(*locator)
                        for element in elements:
                            element_text = element.text.strip()
                            # Check if the text contains the order number
                            if str(expected_order_number) in element_text:
                                return True
                            # Also try to parse as integer
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
