from selenium.webdriver.common.by import By


class MainPageLocators:
    """Локаторы для главной страницы Burger Palace"""

    # Навигация и header
    HEADER_SECTION = (By.XPATH, "//header[contains(@class,'AppHeader_header__')]")
    ACCOUNT_BUTTON = (By.XPATH, "//a[contains(@href, '/account') and @role='button']")
    CONSTRUCTOR_TAB = (By.XPATH, "//a[contains(@href, '/') and .//p[text()='Конструктор']]")
    ORDERS_FEED_TAB = (
        By.XPATH,
        "//a[contains(@href, '/feed') and .//p[contains(text(), 'Лента Заказов')]]"
    )
    APP_LOGO = (By.XPATH, "//div[contains(@class, 'AppHeader_header__logo__')]")

    # Конструктор бургеров
    INGREDIENTS_SECTION = (By.XPATH, "//section[contains(@class, 'BurgerIngredients_ingredients__')]")
    BUNS_CATEGORY = (By.XPATH, "//button[.//span[text()='Булки'] and @role='tab']")
    SAUCES_CATEGORY = (By.XPATH, "//button[.//span[text()='Соусы'] and @role='tab']")
    FILLINGS_CATEGORY = (By.XPATH, "//button[.//span[text()='Начинки'] and @role='tab']")

    # Ингредиенты
    CRATER_BUN_ITEM = (
        By.XPATH,
        "//div[contains(@class, 'IngredientCard_card__')]//img[contains(@alt, 'Краторная булка')]"
    )
    INGREDIENT_COUNTER = (By.XPATH, "//div[contains(@class, 'counter_counter__')]//p")

    # Конструктор заказа
    CONSTRUCTOR_AREA = (By.XPATH, "//section[contains(@class, 'BurgerConstructor_basket__')]")
    PLACE_ORDER_BUTTON = (By.XPATH, "//button[contains(text(), 'Оформить заказ')]")
    ORDER_TOTAL = (By.XPATH, "//div[contains(@class, 'OrderTotal_total__')]//p")

    # Модальные окна
    ORDER_DETAILS_MODAL = (
        By.XPATH, "//div[contains(@class, 'Modal_modal__') and .//h2[contains(text(), 'идентификатор заказа')]]")
    MODAL_CLOSE_BUTTON = (By.XPATH, "//button[contains(@class, 'Modal_close__')]//*[local-name()='svg']")
    ORDER_NUMBER = (By.XPATH, "//h2[contains(@class, 'Modal_modal__title__') and contains(text(), '#')]")

    # Лента заказов
    ORDER_FEED_SECTION = (By.XPATH, "//section[contains(@class, 'OrderFeed_feed__')]")
    ORDER_FEED_TITLE = (By.XPATH, "//h1[text()='Лента заказов']")
    ORDER_ITEMS_LIST = (By.XPATH, "//ul[contains(@class, 'OrderFeed_list__')]/li")
    FIRST_ORDER_ITEM = (By.XPATH, "//ul[contains(@class, 'OrderFeed_list__')]/li[1]")

    # Статистика заказов
    ORDERS_TOTAL = (By.XPATH, "//p[contains(text(), 'Выполнено за все время')]/following-sibling::p")
    ORDERS_TODAY = (By.XPATH, "//p[contains(text(), 'Выполнено за сегодня')]/following-sibling::p")
    ORDERS_IN_PROGRESS = (By.XPATH, "//div[contains(text(), 'В работе:')]/following-sibling::ul//li")

    # Состояния и индикаторы
    LOADING_INDICATOR = (By.XPATH, "//div[contains(@class, 'Modal_modal__loading__')]")
    SUCCESS_ORDER_INDICATOR = (By.XPATH, "//div[contains(text(), 'Заказ создан успешно')]")