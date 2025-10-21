import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Поиск элемента")
    def find_element(self, locator):
        return self.driver.find_element(*locator)

    @allure.step("Получение текста элемента")
    def text_of_element(self, locator):
        return self.driver.find_element(*locator).text

    @allure.step("Клик по элементу")
    def click_on_element(self, locator):
        self.driver.find_element(*locator).click()

    @allure.step("Заполнение поля ввода")
    def fill_input(self, locator, text):
        self.wait_visibility_of_element(locator)
        self.driver.find_element(*locator).send_keys(text)

    @allure.step("Ожидание видимости элемента")
    def wait_visibility_of_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    @allure.step("Ожидание появления текста в элементе")
    def wait_text_of_element(self, locator, text):
        return WebDriverWait(self.driver, 10).until(
            expected_conditions.text_to_be_present_in_element(locator, text)
        )

    @allure.step("Ожидание кликабельности элемента")
    def wait_for_element_to_be_clickable(self, locator):
        return WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(locator)
        )

    @allure.step("Закрытие модального окна")
    def wait_order_modal_window_closed(self, locator):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.invisibility_of_element(locator)
        )

    @allure.step("Прокрутка к элементу")
    def scroll_to_element(self, locator):
        self.driver.execute_script(
            "arguments[0].scrollIntoView();", self.driver.find_element(*locator)
        )

    @allure.step("Проверка видимости элемента")
    def visibility_of_element(self, locator):
        return self.driver.find_element(*locator).is_displayed()

    @allure.step("Получение текущего дескриптора окна")
    def current_window_handle(self):
        return self.driver.current_window_handle

    @allure.step("Ожидание")
    def wait(self):
        return WebDriverWait(self.driver, 10)

    @allure.step("Получение всех дескрипторов окон")
    def window_handles(self):
        return self.driver.window_handles

    @allure.step("Переключение на окно")
    def switch_to_window(self, window):
        self.driver.switch_to.window(window)

    @allure.step("Получение текущего URL")
    def current_url(self):
        return self.driver.current_url

    @allure.step("Перетаскивание элемента")
    def move_element(self, locator_source, locator_target):
        source = self.driver.find_element(*locator_source)
        target = self.driver.find_element(*locator_target)
        action = ActionChains(self.driver)
        action.drag_and_drop(source, target).pause(5).perform()