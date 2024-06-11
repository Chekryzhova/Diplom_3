from pages.base_page import BasePage
from locators.auth_page_locators import AuthPageLocators
from data import StellarBurgerData
import allure

class AuthPage(BasePage):

    @allure.step('Нажимаем кнопку "Восстановить пароль"')
    def click_recovery_password_button(self):
        recovery_password_button = self.driver.find_element(*AuthPageLocators.RECOVER_PASSWORD_BUTTON)
        self.driver.execute_script("arguments[0].click();", recovery_password_button)

    @allure.step('Вводим емейл для восстановления пароля')
    def input_email_for_recovery_password(self):
        email = self.driver.find_element(*AuthPageLocators.EMAIL)
        email.send_keys(StellarBurgerData.EMAIL_RECOVERY_PASSWORD)

    @allure.step('Жмём на кнопку "Восстановить"')
    def click_recovery_button(self):
        recovery_button = self.driver.find_element(*AuthPageLocators.RECOVERY_BUTTON)
        self.driver.execute_script("arguments[0].click();", recovery_button)

    @allure.step('Жмём на кнопку показать/скрыть пароль')
    def click_hide_password_button(self):
        hide_password = self.driver.find_element(*AuthPageLocators.HIDE_PASSWORD)
        self.driver.execute_script("arguments[0].click();", hide_password)

    @allure.step('Вводим емейл для авторизации')
    def input_email_for_authorization(self):
        email = self.driver.find_element(*AuthPageLocators.LOGIN_EMAIL_INPUT)
        email.send_keys(StellarBurgerData.CREATE_USER_BODY["email"])

    @allure.step('Вводим пароль для авторизации')
    def input_password_for_authorization(self):
        password = self.driver.find_element(*AuthPageLocators.LOGIN_PASSWORD_INPUT)
        password.send_keys(StellarBurgerData.CREATE_USER_BODY["password"])

    @allure.step('Жмём кнопку "Войти"')
    def click_login_button(self):
        login_button = self.driver.find_element(*AuthPageLocators.LOGIN_BUTTON)
        self.driver.execute_script("arguments[0].click();", login_button)






