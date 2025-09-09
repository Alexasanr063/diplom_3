import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
from selenium.webdriver.common.keys import Keys


class BurgerBasePage:
    """Базовый класс страницы для всех страниц Burger Palace"""

    def __init__(self, driver):
        self.driver = driver
        self.default_timeout = 15
        self.short_timeout = 5

    @allure.step("Поиск элемента на странице: {locator}")
    def find_element(self, locator, timeout=None):
        """Найти элемент с ожиданием его появления"""
        timeout = timeout or self.short_timeout
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
        except TimeoutException:
            allure.attach(f"Элемент {locator} не найден за {timeout} секунд", name="Element Not Found")
            raise

    @allure.step("Получить текст элемента: {locator}")
    def text_of_element(self, locator):
        """Получить текст элемента"""
        element = self.find_element(locator)
        return element.text.strip()

    @allure.step("Клик по элементу: {locator}")
    def click_on_element(self, locator, timeout=None):
        """Кликнуть по элементу с ожиданием кликабельности"""
        timeout = timeout or self.default_timeout
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
        try:
            element.click()
        except Exception:
            # Fallback: клик через JavaScript
            self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Заполнение поля: {locator} -> '{text}'")
    def fill_input(self, locator, text, clear_existing=True):
        """Заполнить текстовое поле"""
        element = self.wait_visibility_of_element(locator)
        if clear_existing:
            element.clear()
        element.send_keys(text)

    @allure.step("Ожидание видимости элемента: {locator}")
    def wait_visibility_of_element(self, locator, timeout=None):
        """Ожидать появления видимого элемента"""
        timeout = timeout or self.default_timeout
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    @allure.step("Ожидание текста в элементе: {locator} -> '{text}'")
    def wait_text_of_element(self, locator, text, timeout=None):
        """Ожидать появления определенного текста в элементе"""
        timeout = timeout or self.default_timeout
        return WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(locator, text)
        )

    @allure.step("Ожидание кликабельности элемента: {locator}")
    def wait_for_element_to_be_clickable(self, locator, timeout=None):
        """Ожидать пока элемент станет кликабельным"""
        timeout = timeout or self.default_timeout
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    @allure.step("Ожидание исчезновения элемента: {locator}")
    def wait_order_modal_window_closed(self, locator, timeout=None):
        """Ожидать исчезновения элемента"""
        timeout = timeout or self.short_timeout
        return WebDriverWait(self.driver, timeout).until(
            EC.invisibility_of_element_located(locator)
        )

    @allure.step("Скролл к элементу: {locator}")
    def scroll_to_element(self, locator):
        """Проскроллить к элементу"""
        element = self.find_element(locator)
        self.driver.execute_script(
            "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",
            element
        )

    @allure.step("Проверка видимости элемента: {locator}")
    def visibility_of_element(self, locator, timeout=None):
        """Проверить виден ли элемент"""
        try:
            self.wait_visibility_of_element(locator, timeout or self.short_timeout)
            return True
        except TimeoutException:
            return False

    @allure.step("Перетаскивание элемента: {source_locator} -> {target_locator}")
    def move_element(self, source_locator, target_locator):
        """Перетащить элемент из source в target"""
        source = self.find_element(source_locator)
        target = self.find_element(target_locator)

        action = ActionChains(self.driver)
        action.drag_and_drop(source, target).pause(1).perform()

    @allure.step("Наведение курсора на элемента: {locator}")
    def hover_over_element(self, locator):
        """Навести курсор на элемент"""
        element = self.find_element(locator)
        action = ActionChains(self.driver)
        action.move_to_element(element).pause(0.5).perform()

    @allure.step("Получение текущего URL")
    def current_url(self):
        """Получить текущий URL страницы"""
        return self.driver.current_url

    @allure.step("Переключение на новое окно")
    def switch_to_window(self, window):
        """Переключиться на новое окно браузера"""
        handles = self.driver.window_handles
        if len(handles) > 1:
            self.driver.switch_to.window(handles[-1])

    @allure.step("Закрытие текущего окна и возврат к предыдущему")
    def close_current_window(self):
        """Закрыть текущее окно и вернуться к предыдущему"""
        handles = self.driver.window_handles
        if len(handles) > 1:
            self.driver.close()
            self.driver.switch_to.window(handles[0])

    @allure.step("Обновление страницы")
    def refresh_page(self):
        """Обновить текущую страницу"""
        self.driver.refresh()
        self.wait_for_page_loaded()

    @allure.step("Ожидание загрузки страницы")
    def wait_for_page_loaded(self, timeout=None):
        """Ожидать полной загрузки страницы"""
        timeout = timeout or self.default_timeout
        WebDriverWait(self.driver, timeout).until(
            lambda driver: driver.execute_script("return document.readyState") == "complete"
        )

    @allure.step("Нажатие клавиши Escape")
    def press_escape(self):
        """Нажать клавишу Escape"""
        action = ActionChains(self.driver)
        action.send_keys(Keys.ESCAPE).perform()

    @allure.step("Сделать скриншот")
    def take_screenshot(self, name="screenshot"):
        """Сделать скриншот и прикрепить к Allure отчету"""
        allure.attach(
            self.driver.get_screenshot_as_png(),
            name=name,
            attachment_type=allure.attachment_type.PNG
        )