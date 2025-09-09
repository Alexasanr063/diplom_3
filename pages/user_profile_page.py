import allure
from diplom_3.locators.auth_locators import AuthPageLocators
from diplom_3.locators.recovery_locators import UserAccountLocators
from diplom_3.locators.constructor_locators import MainPageLocators
from diplom_3.locators.user_profile_locators import PasswordRecoveryLocators
from diplom_3.pages.base_core_page import BurgerBasePage


class UserProfilePage(BurgerBasePage):
    """Страница личного кабинета пользователя Burger Palace"""

    def __init__(self, driver):
        super().__init__(driver)
        self.constructor_locators = MainPageLocators()
        self.profile_locators = PasswordRecoveryLocators()
        self.auth_locators = AuthPageLocators()

    @allure.step("Открытие личного кабинета")
    def open_user_profile(self):
        """Открыть личный кабинет пользователя"""
        self.click_on_element(self.constructor_locators.ACCOUNT_BUTTON)
        self.wait_for_profile_loaded()

    @allure.step("Ожидание загрузки личного кабинета")
    def wait_for_profile_loaded(self):
        """Ожидать полной загрузки личного кабинета"""
        self.wait_visibility_of_element(self.profile_locators.PROFILE_FORM)

    @allure.step("Переход в раздел профиля")
    def go_to_profile_section(self):
        """Перейти в раздел профиля"""
        self.click_on_element(self.profile_locators.PROFILE_LINK)
        self.wait_visibility_of_element(self.profile_locators.NAME_INPUT)

    @allure.step("Переход в историю заказов")
    def go_to_order_history(self):
        """Перейти в раздел истории заказов"""
        self.click_on_element(self.profile_locators.ORDER_HISTORY_LINK)
        self.wait_for_order_history_loaded()

    @allure.step("Ожидание загрузки истории заказов")
    def wait_for_order_history_loaded(self):
        """Ожидать загрузки раздела истории заказов"""
        self.wait_visibility_of_element(self.profile_locators.ORDERS_SECTION)

    @allure.step("Выход из системы")
    def logout(self):
        """Выйти из системы"""
        self.click_on_element(self.profile_locators.LOGOUT_BUTTON)
        self.wait_for_logout_complete()

    @allure.step("Ожидание завершения выхода")
    def wait_for_logout_complete(self):
        """Ожидать завершения процесса выхода из системы"""
        self.wait_visibility_of_element(self.auth_locators.SIGN_IN_BUTTON)

    @allure.step("Обновление данных профиля")
    def update_profile(self, name=None, email=None, password=None):
        """Обновить данные профиля пользователя"""
        if name:
            self.fill_input(self.profile_locators.NAME_INPUT, name)
        if email:
            self.fill_input(self.profile_locators.EMAIL_INPUT, email)
        if password:
            self.fill_input(self.profile_locators.PASSWORD_INPUT, password)

        self.click_on_element(self.profile_locators.SAVE_CHANGES_BUTTON)
        self.wait_for_save_confirmation()

    @allure.step("Ожидание подтверждения сохранения")
    def wait_for_save_confirmation(self):
        """Ожидать подтверждения сохранения изменений"""
        self.wait_visibility_of_element(self.profile_locators.SUCCESS_SAVE_MESSAGE, timeout=10)

    @allure.step("Проверка видимости истории заказов")
    def is_order_history_visible(self):
        """Проверить видна ли история заказов"""
        return self.visibility_of_element(self.profile_locators.ORDERS_SECTION)

    @allure.step("Получение количества заказов в истории")
    def get_orders_count(self):
        """Получить количество заказов в истории"""
        order_elements = self.driver.find_elements(*self.profile_locators.ORDER_ITEMS)
        return len(order_elements)

    @allure.step("Проверка авторизации пользователя")
    def is_user_authenticated(self):
        """Проверить авторизован ли пользователь"""
        return self.visibility_of_element(self.profile_locators.PROFILE_FORM)

    @allure.step("Открытие деталей заказа")
    def open_order_details(self, order_index=0):
        """Открыть детали конкретного заказа"""
        order_elements = self.driver.find_elements(*self.profile_locators.ORDER_ITEMS)
        if order_index < len(order_elements):
            order_elements[order_index].click()
            # Здесь может быть ожидание модального окна с деталями

    @allure.step("Проверка активности раздела профиля")
    def is_profile_section_active(self):
        """Проверить активен ли раздел профиля"""
        element = self.find_element(self.profile_locators.PROFILE_LINK)
        return "profile__link_active__" in element.get_attribute("class")