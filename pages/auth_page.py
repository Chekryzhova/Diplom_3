from pages.base_page import BasePage
from locators.auth_page_locators import AuthPageLocators
from data import StellarBurgerData
import allure
import urls

class AuthPage(BasePage):

    @allure.step('Нажимаем кнопку "Восстановить пароль"')
    def click_recovery_password_button(self):
        self.click_element(AuthPageLocators.RECOVER_PASSWORD_BUTTON)

    @allure.step('Вводим емейл для восстановления пароля')
    def input_email_for_recovery_password(self):
        self.input(AuthPageLocators.EMAIL, StellarBurgerData.EMAIL_RECOVERY_PASSWORD)

    @allure.step('Жмём на кнопку "Восстановить"')
    def click_recovery_button(self):
        self.click_element(AuthPageLocators.RECOVERY_BUTTON)

    @allure.step('Находим на странице кнопку сохранить')
    def find_save_button(self):
        return self.find_element(AuthPageLocators.SAVE_BUTTON)

    @allure.step('Ждём повления кнопки показать/скрыть пароль')
    def wait_hide_password_button(self):
        self.wait_element_to_be_clickable(AuthPageLocators.HIDE_PASSWORD_BUTTON)

    @allure.step('Ждём выделения поля пароль')
    def wait_highlight_password_field(self):
        return self.wait_visibility_of_element_located(AuthPageLocators.HIGHLIGHTED_PASSWORD)


    @allure.step('Жмём на кнопку показать/скрыть пароль')
    def click_hide_password_button(self):
        self.click_element(AuthPageLocators.HIDE_PASSWORD)


    @allure.step('Вводим емейл для авторизации')
    def input_email_for_authorization(self):
        self.input(AuthPageLocators.LOGIN_EMAIL_INPUT, StellarBurgerData.CREATE_USER_BODY["email"])

    @allure.step('Вводим пароль для авторизации')
    def input_password_for_authorization(self):
        self.input(AuthPageLocators.LOGIN_PASSWORD_INPUT, StellarBurgerData.CREATE_USER_BODY["password"])


    @allure.step('Жмём кнопку "Войти"')
    def click_login_button(self):
        self.click_element(AuthPageLocators.LOGIN_BUTTON)

    @allure.step('Жмём перехода со страницы авторизации')
    def wait_changing_url_from_auth_page(self):
        self.wait_change_url(urls.BURGER + urls.LOGIN)

    @allure.step('Находим на странице кнопку войти')
    def find_login_button(self):
        return self.find_element(AuthPageLocators.LOGIN_BUTTON)

    @allure.step('Находим на странице кнопку восстановить')
    def find_recovery_button(self):
        return self.find_element(AuthPageLocators.RECOVERY_BUTTON)







