from selenium.webdriver.common.by import By
class AuthPageLocators:

    RECOVER_PASSWORD_BUTTON = (By.XPATH, "//a[@href='/forgot-password']")
    RECOVERY_BUTTON = (By.XPATH, "//button[text() = 'Восстановить']")
    EMAIL = (By.XPATH, "//input[@class = 'text input__textfield text_type_main-default']")
    SAVE_BUTTON = (By.XPATH, "//button[@class = 'button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']")
    HIDE_PASSWORD = (By.XPATH, "//input[@type='password']/following-sibling::div[@class='input__icon input__icon-action']")
    HIGHLIGHTED_PASSWORD = (By.XPATH, ".//div[@class='input pr-6 pl-6 input_type_text input_size_default input_status_active']")
    LOGIN_EMAIL_INPUT = (By.XPATH, "//input[@name = 'name']")
    LOGIN_PASSWORD_INPUT = (By.XPATH, ".//input[@name = 'Пароль']")
    LOGIN_BUTTON = (By.XPATH, "//button[text() = 'Войти']")



