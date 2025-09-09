from diplom_3.locators.main_page_locators import BurgerAppLocators
from diplom_3.pages.base_page import BasePage
import allure


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.main_page_locators = BurgerAppLocators()

    @allure.step("Клик по кнопке конструктора")
    def click_in_constructor(self):
        self.click_on_element(self.main_page_locators.CONSTRUCTOR_LINK)

    @allure.step("Клик по кнопке оформления заказа")
    def make_order(self):
        self.click_on_element(self.main_page_locators.PLACE_ORDER_BUTTON)

    @allure.step("Проверка видимости ссылки на булки")
    def buns_link_is_visible(self):
        return self.visibility_of_element(self.main_page_locators.BUNS_LINK)

    @allure.step("Клик по ссылке ленты заказов")
    def click_in_order_feed(self):
        self.click_on_element(self.main_page_locators.ORDERS_FEED_LINK)

    @allure.step("Проверка видимости заголовка ленты заказов")
    def order_feed_header_is_visible(self):
        return self.visibility_of_element(self.main_page_locators.ORDER_FEED_HEADER)

    @allure.step("Ожидание видимости заголовка ленты заказов")
    def wait_for_order_feed_header(self):
        self.wait_visibility_of_element(self.main_page_locators.ORDER_FEED_HEADER)

    @allure.step("Клик по краторной булке")
    def click_on_crater_bun(self):
        self.click_on_element(self.main_page_locators.CRATER_BUN)

    @allure.step("Закрытие модального окна")
    def close_modal_window(self):
        self.click_on_element(self.main_page_locators.CLOSE_MODAL_WINDOW_BUTTON)

    @allure.step("Ожидание появления модального окна")
    def wait_for_modal_window(self):
        self.wait_visibility_of_element(
            self.main_page_locators.CLOSE_MODAL_WINDOW_BUTTON
        )

    @allure.step("Ожидание видимости краторной булки")
    def wait_for_bun(self):
        self.wait_visibility_of_element(self.main_page_locators.CRATER_BUN)

    @allure.step("Видимость кнопки закрытия модального окна")
    def close_modal_window_button_is_visible(self):
        return self.visibility_of_element(
            self.main_page_locators.CLOSE_MODAL_WINDOW_BUTTON
        )

    @allure.step("Перетаскивание булки в область ингредиентов")
    def drag_and_drop_bun(self):
        self.move_element(
            self.main_page_locators.CRATER_BUN,
            self.main_page_locators.BURGER_INGREDIENTS,
        )

    @allure.step("Проверка видимости счетчика булок")
    def bun_counter_is_visible(self):
        return self.visibility_of_element(self.main_page_locators.BUN_COUNTER)

    @allure.step("Проверка видимости кнопки оформления заказа")
    def place_order_button_is_visible(self):
        return self.visibility_of_element(self.main_page_locators.PLACE_ORDER_BUTTON)

    @allure.step("Ожидание видимости номера заказа")
    def wait_for_made_order_modal_window(self):
        self.wait_visibility_of_element(self.main_page_locators.ORDER_ID)

    @allure.step("Видимость номера заказа")
    def order_id_is_visible(self):
        return self.visibility_of_element(self.main_page_locators.ORDER_ID)