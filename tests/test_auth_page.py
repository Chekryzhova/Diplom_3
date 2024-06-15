from pages.home_page import HomePage
from pages.auth_page import AuthPage
import allure


class TestAuthPage:

    @allure.title('Проверяем ввод почты и клик по кнопке «Восстановить»')
    @allure.description('Нажимаем на кнопку восстановить пароль, вводим почту и жмём на кнопку восстановить')
    def test_input_email_for_recovery_password(self, driver):
        home_page = HomePage(driver)
        auth_page = AuthPage(driver)
        home_page.click_login_to_account_button()
        auth_page.click_recovery_password_button()
        auth_page.input_email_for_recovery_password()
        auth_page.click_recovery_button()
        save_button = auth_page.find_save_button()
        assert save_button.is_displayed()

    @allure.title('Проверяем, что клик по кнопке показать/скрыть пароль делает поле активным')
    @allure.description('Нажимаем на кнопку восстановить пароль, вводим почту и жмём на кнопку восстановить. Далее нажимаем на кнопку показать/скрыть пароль')
    def test_highlight_password_field(self, driver):
        home_page = HomePage(driver)
        auth_page = AuthPage(driver)
        home_page.click_login_to_account_button()
        auth_page.click_recovery_password_button()
        auth_page.input_email_for_recovery_password()
        auth_page.click_recovery_button()
        auth_page.wait_hide_password_button()
        auth_page.click_hide_password_button()
        highlight_password_field = auth_page.wait_highlight_password_field()

        assert highlight_password_field.is_displayed()
