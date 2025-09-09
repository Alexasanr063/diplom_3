from diplom_3.locators.constructor_locators import ConstructorLocators
from diplom_3.pages.core_page import BurgerBasePage
import allure


class BurgerConstructorPage(BurgerBasePage):
    """Страница конструктора бургеров Burger Palace"""

    def __init__(self, driver):
        super().__init__(driver)
        self.locators = ConstructorLocators()

    @allure.step("Открытие конструктора бургеров")
    def open_burger_constructor(self):
        """Открыть раздел конструктора бургеров"""
        self.click_element(self.locators.CONSTRUCTOR_TAB)
        self.wait_for_constructor_loaded()

    @allure.step("Ожидание загрузки конструктора")
    def wait_for_constructor_loaded(self):
        """Ожидать полной загрузки конструктора"""
        self.wait_for_element_visible(self.locators.INGREDIENTS_SECTION)
        self.wait_for_element_visible(self.locators.CONSTRUCTOR_AREA)

    @allure.step("Выбор категории ингредиентов: {category}")
    def select_ingredient_category(self, category):
        """Выбрать категорию ингредиентов"""
        category_locators = {
            'buns': self.locators.BUNS_CATEGORY,
            'sauces': self.locators.SAUCES_CATEGORY,
            'fillings': self.locators.FILLINGS_CATEGORY
        }

        if category in category_locators:
            self.click_element(category_locators[category])
            self.wait_for_category_loaded(category)

    @allure.step("Ожидание загрузки категории")
    def wait_for_category_loaded(self, category):
        """Ожидать загрузки выбранной категории"""
        # Можно добавить специфичные проверки для каждой категории
        self.wait_for_element_visible(self.locators.INGREDIENTS_SECTION)

    @allure.step("Добавление краторной булки в конструктор")
    def add_crater_bun_to_constructor(self):
        """Добавить краторную булку в конструктор бургера"""
        self.drag_and_drop(self.locators.CRATER_BUN_INGREDIENT, self.locators.CONSTRUCTOR_AREA)
        self.wait_for_ingredient_added()

    @allure.step("Ожидание добавления ингредиента")
    def wait_for_ingredient_added(self):
        """Ожидать подтверждения добавления ингредиента"""
        # Проверяем появление счетчика или другого индикатора
        self.wait_for_element_visible(self.locators.INGREDIENT_COUNTER, timeout=5)

    @allure.step("Оформление заказа")
    def place_order(self):
        """Оформить заказ"""
        self.click_element(self.locators.PLACE_ORDER_BUTTON)
        self.wait_for_order_modal()

    @allure.step("Ожидание модального окна заказа")
    def wait_for_order_modal(self):
        """Ожидать открытия модального окна с номером заказа"""
        self.wait_for_element_visible(self.locators.ORDER_MODAL)

    @allure.step("Получение номера заказа")
    def get_order_number(self):
        """Получить номер созданного заказа"""
        return self.get_element_text(self.locators.ORDER_NUMBER)

    @allure.step("Закрытие модального окна заказа")
    def close_order_modal(self):
        """Закрыть модальное окно с номером заказа"""
        self.click_element(self.locators.MODAL_CLOSE_BUTTON)
        self.wait_for_element_invisible(self.locators.ORDER_MODAL)

    @allure.step("Проверка видимости кнопки оформления заказа")
    def is_order_button_visible(self):
        """Проверить видна ли кнопка оформления заказа"""
        return self.is_element_visible(self.locators.PLACE_ORDER_BUTTON)

    @allure.step("Проверка активности конструктора")
    def is_constructor_tab_active(self):
        """Проверить активен ли таб конструктора"""
        element = self.find_element(self.locators.CONSTRUCTOR_TAB)
        return "tab_tab_type_current__" in element.get_attribute("class")

    @allure.step("Получение общей стоимости заказа")
    def get_order_total(self):
        """Получить общую стоимость текущего заказа"""
        return self.get_element_text(self.locators.ORDER_TOTAL)

    @allure.step("Очистка конструктора")
    def clear_constructor(self):
        """Очистить конструктор от добавленных ингредиентов"""
        # Реализация зависит от функционала приложения
        # Можно обновить страницу или использовать специальную кнопку
        self.refresh_page()
        self.wait_for_constructor_loaded()

    @allure.step("Проверка наличия ингредиентов в конструкторе")
    def has_ingredients_in_constructor(self):
        """Проверить есть ли ингредиенты в конструкторе"""
        try:
            # Ищем элементы ингредиентов в области конструктора
            ingredients = self.driver.find_elements(
                *self.locators.CONSTRUCTOR_AREA
            )
            return len(ingredients) > 0
        except Exception:
            return False