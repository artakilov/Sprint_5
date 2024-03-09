from selenium.webdriver.common.by import By


class TestLocators:
    # кнопка "Личный кабинет" в хедере
    BUTTON_PERSONAL_ACCOUNT = By.XPATH, '//*[contains (text(), "Личный Кабинет")]'
    # кнопка "Войти в аккаунт" на главной странице
    BUTTON_LOGIN_TO_ACCOUNT = By.XPATH, '//*[contains(@class, "button_button_size_large")]'
    # ссылка "Войти" на странице регистрации
    LINK_LOGIN_IN_REGISTRATION = By.XPATH, '//*[@href="/login"]'
    # ссылка "Войти" на странице восстановления пароля
    LINK_LOGIN_IN_RESTORE_PASSWORD = By.XPATH, '//*[@href="/login"]'
    # поле "Email" на странице "Вход"
    FIELD_LOGIN_EMAIL = By.XPATH, '//input[@name="name"]'
    # поле "Пароль" на странице "Вход"
    FIELD_LOGIN_PASSWORD = By.XPATH, '//input[@name="Пароль"]'
    # ссылка "Зарегистрироваться"
    LINK_REGISTRATION = By.XPATH, '//*[@href="/register"]'
    # ссылка "Восстановить пароль"
    LINK_RESTORE_PASSWORD = By.XPATH, '//*[@href="/forgot-password"]'
    # поле "Имя" на странице "Регистрация"
    FIELD_REGISTRATION_NAME = By.XPATH, '//label[text()="Имя"]/following-sibling::input'
    # поле "Email" на странице "Регистрация"
    FIELD_REGISTRATION_EMAIL = By.XPATH, '//label[text()="Email"]/following-sibling::input'
    # поле "Пароль" на странице "Регистрация"
    FIELD_REGISTRATION_PASSWORD = By.XPATH, '//label[text()="Пароль"]/following-sibling::input'
    # кнопка "Зарегистрироваться"
    BUTTON_REGISTRATION = By.XPATH, '//*[text()="Зарегистрироваться"]'
    # кнопка "Конструктор" в хедере
    BUTTON_CONSTRUCTOR = By.XPATH, '//ul[contains(@class, "AppHeader_header")]/li[1]'
    # логотип "Stellar Burgers" в хедере
    LINK_LOGO = By.XPATH, '//*[contains(@class, "AppHeader_header__logo")]'
    # раздел "Булки" в конструкторе
    CHAPTER_BUNS = By.XPATH, '//span[text()="Булки"]/parent::div'
    # раздел "Соусы" в конструкторе
    CHAPTER_SAUCES = By.XPATH, '//span[text()="Соусы"]/parent::div'
    # раздел "Начинки" в конструкторе
    CHAPTER_FILLINGS = By.XPATH, '//span[text()="Начинки"]/parent::div'
    # раздел "Булки" в списке
    LIST_BUNS = By.XPATH, '//h2[text()="Булки"]'
    # раздел "Соусы" в списке
    LIST_SAUCES = By.XPATH, '//h2[text()="Соусы"]'
    # раздел "Начинки" в списке
    LIST_FILLINGS = By.XPATH, '//h2[text()="Начинки"]'
    # кнопка "Выйти" в личном кабинете
    BUTTON_LOGOUT = By.XPATH, '//*[text()="Выход"]'
    # кнопка "Профиль" в личном кабинете
    BUTTON_PROFILE = By.XPATH, '//*[text()="Профиль"]'
    # кнопка "Войти" на странице Вход
    BUTTON_LOGIN = By.XPATH, '//*[text()="Войти"]'
    # кнопка "Оформить заказ" на главной странице
    BUTTON_CHECKOUT = By.XPATH, '//*[text()="Оформить заказ"]'
    # надпись "Некорректный пароль"
    LABEL_INCORRECT_PASSWORD = By.XPATH, '//*[text()="Некорректный пароль"]'
