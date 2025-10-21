from selenium.webdriver.common.by import By


class BurgerAppLocators:
    # "Personal Account" button on main page
    ACCOUNT_LINK = (By.XPATH, "//a[@href = '/account']")

    CONSTRUCTOR_LINK = (By.XPATH, "//p[text()='Конструктор']")
    ORDERS_FEED_LINK = (
        By.XPATH,
        '//p[contains(@class, "AppHeader_header__linkText__3q_va") and text()="Лента Заказов"]',
    )

    # Order feed
    FIRST_ORDER_IN_FEED = (By.XPATH, "//ul[contains(@class,'OrderFeed_list')]/li[1]")
    ORDER_DETAILS_MODAL = (
        By.XPATH,
        '//div[@class="Modal_orderBox__1xWdi Modal_modal__contentBox__sCy8X p-10"]',
    )
    ORDER_FEED_HEADER = (By.XPATH, "//h1[normalize-space()='Лента заказов']")
    MY_ORDER_IN_ORDER_FEED = (
        By.XPATH,
        "//p[contains(@class, 'text') and contains(@class, 'text_type_main-default') and text()='Выполнен']",
    )
    ORDERS_FOR_ALL_TIME = (
        By.XPATH,
        '//p[contains(normalize-space(),"Выполнено за все время")]/following-sibling::p[1]',
    )
    ORDERS_FOR_TODAY = (
        By.XPATH,
        '//p[contains(normalize-space(),"Выполнено за сегодня")]/following-sibling::p[1]',
    )
    ORDER_IN_PROCESS_IN_FEED = (
        By.XPATH,
        '//div/ul[2]/li[contains(@class,"text_type_digits-default")]',
    )
    ORDER_IN_MODAL_WINDOW = (
        By.XPATH,
        '//h2[@class="Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8"]',
    )
    MODAL_OPENED = (
        By.XPATH,
        "//section[contains(@class,'Modal_modal_opened') and .//div[contains(@class,'Modal_orderBox')]]",
    )
    CRATER_BUN = (
        By.XPATH,
        "//img[contains(@alt,'Краторная') and contains(@alt,'N-200i')]",
    )
    CLOSE_MODAL_WINDOW_BUTTON = (By.XPATH, '//button/*[name()="svg"]')
    BURGER_INGREDIENTS = (
        By.XPATH,
        '//ul[@class="BurgerConstructor_basket__list__l9dp_"]',
    )
    BUN_COUNTER = (By.XPATH, '//p[text()="2"]')
    ORDER_ID = (By.XPATH, '//p[text()="идентификатор заказа"]')
    PLACE_ORDER_BUTTON = (By.XPATH, '//button[text()="Оформить заказ"]')
    EXTRA_ORDER_MODAL_WINDOW = (By.CLASS_NAME, "Modal_modal__loading__3534A")

    SAUCES_LINK = (By.XPATH, "//span[text() = 'Соусы']")
    BUNS_LINK = (By.XPATH, "//span[text() = 'Булки']")
    FILLINGS_LINK = (By.XPATH, "//span[text() = 'Начинки']")
