from selenium.webdriver.common.by import By


class PersovalAccountPageLocators:

    TITLE_PROFILE = (By.XPATH, "//a[text() = 'Профиль']")
    ORDER_HISTORY = (By.XPATH, "//a[@href = '/account/order-history']")
    LOGOUT_BUTTON = (By.XPATH, "//button[text() = 'Выход']")
    ORDER_NUMBER = (By.XPATH, "//p[@class = 'text text_type_digits-default']")

