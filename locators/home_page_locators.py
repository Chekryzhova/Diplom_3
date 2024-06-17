from selenium.webdriver.common.by import By


class HomePageLocators:

    LOGIN_TO_ACCOUNT_BUTTON = (By.XPATH, "//button[text() = 'Войти в аккаунт']")
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//a[@href = '/account']")
    CONSTRUCTOR_BUTTON = (By.XPATH, "//a[@class = 'AppHeader_header__link__3D_hX' and @href = '/']/p[text() = 'Конструктор']")
    ORDER_FEED_BUTTON = (By.XPATH, "//a[@href = '/feed']")
    FLUORESCENT_BUN = (By.XPATH, "//a[@href = '/ingredient/61c0c5a71d1f82001bdaaa6d']")
    CLOSE_INGREDIENT_INFO_BUTTON = (By.XPATH, "//div[@class = 'Modal_modal__contentBox__sCy8X pt-10 pb-15']/following-sibling::button[@class = 'Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']")
    ADD_INGREDIENT_TO_ORDER = (By.XPATH, "//span[text() = 'Перетяните булочку сюда (низ)']")
    INGREDIENT_COUNTER = (By.XPATH, "//a[@href = '/ingredient/61c0c5a71d1f82001bdaaa6d']/div[@class = 'counter_counter__ZNLkj counter_default__28sqi']/p[text() = '2']")
    CONSTRUCTOR = (By.XPATH, "//h1[text() = 'Соберите бургер']")
    PLACE_ORDER_BUTTON = (By.XPATH, "//button[text() = 'Оформить заказ']")
    ORDER_ID = (By.XPATH, "//p[text() = 'идентификатор заказа']")
    CLOSE_ORDER_POPUP = (By.XPATH, "//div[@class = 'Modal_modal__container__Wo2l_']/button[@class = 'Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']")
    LOGO_BUTTON = (By.XPATH, "//div[@class = 'AppHeader_header__logo__2D0X2']/a[@href = '/']")
    ORDER_ID = (By.XPATH, "//h2[@class = 'Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8']")

