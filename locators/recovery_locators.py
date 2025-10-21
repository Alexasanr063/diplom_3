from selenium.webdriver.common.by import By


class UserAccountLocators:
    """Локаторы для личного кабинета пользователя Burger Palace"""

    # Навигация профиля
    ACCOUNT_SIDEBAR = (By.XPATH, "//nav[contains(@class, 'Profile_profile__nav__')]")
    PROFILE_LINK = (By.XPATH, "//a[contains(@href, '/account/profile') and contains(text(), 'Профиль')]")
    ORDER_HISTORY_LINK = (By.XPATH, "//a[contains(@href, '/account/orders') and contains(text(), 'История заказов')]")
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(), 'Выйти из системы')]")

    # Форма профиля
    ACCOUNT_FORM = (By.XPATH, "//form[contains(@class, 'Profile_profile__form__')]")
    NAME_INPUT = (By.XPATH, "//input[@name='name' and @type='text']")
    EMAIL_INPUT = (By.XPATH, "//input[@name='email' and @type='email']")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='password' and @type='password']")

    # Кнопки действий
    SAVE_PROFILE_BUTTON = (By.XPATH, "//button[contains(text(), 'Сохранить изменения')]")
    CANCEL_BUTTON = (By.XPATH, "//button[contains(text(), 'Отмена')]")
    EDIT_PROFILE_BUTTON = (By.XPATH, "//button[contains(text(), 'Редактировать профиль')]")

    # История заказов
    ORDERS_SECTION = (By.XPATH, "//section[contains(@class, 'OrderHistory_orders__')]")
    ORDER_CARDS = (By.XPATH, "//div[contains(@class, 'OrderHistory_order__')]")
    FIRST_ORDER_ITEM = (By.XPATH, "//div[contains(@class, 'OrderHistory_order__')][1]")
    ORDER_NUMBER_LINK = (By.XPATH, "//a[contains(@class, 'OrderHistory_link__')]")
    ORDER_STATUS = (By.XPATH, "//p[contains(@class, 'OrderHistory_status__')]")
    ORDER_DATE = (By.XPATH, "//p[contains(@class, 'OrderHistory_date__')]")
    ORDER_TOTAL = (By.XPATH, "//p[contains(@class, 'OrderHistory_total__')]")

    # Сообщения и статусы
    PROFILE_SAVE_SUCCESS = (By.XPATH, "//div[contains(text(), 'Данные успешно сохранены')]")
    ERROR_MESSAGE = (By.XPATH, "//p[contains(@class, 'input__error-text')]")
    LOADING_INDICATOR = (By.XPATH, "//div[contains(@class, 'Profile_loading__')]")

    # Дополнительные элементы
    USER_AVATAR = (By.XPATH, "//div[contains(@class, 'Profile_avatar__')]//img")
    PERSONAL_DISCOUNT = (By.XPATH, "//div[contains(text(), 'Ваша персональная скидка')]")
    LOYALTY_POINTS = (By.XPATH, "//p[contains(text(), 'Баллы лояльности')]")