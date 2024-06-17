from pages.home_page import HomePage
from pages.auth_page import AuthPage
from pages.personal_account_page import PersonalAccountPage
import allure



class TestPersonalAccount:

    @allure.title('Проверяем открытие личного кабинета')
    @allure.description('Создаём в фикстуре тестовый аккаунт, авторизуемся им в тесте и заходим в личный кабинет. После проверки аккаунт удаляется в фикстуре')
    def test_open_personal_account(self, user, driver):
        home_page = HomePage(driver)
        auth_page = AuthPage(driver)
        personal_account_page = PersonalAccountPage(driver)
        home_page.click_login_to_account_button()
        auth_page.input_email_for_authorization()
        auth_page.input_password_for_authorization()
        auth_page.click_login_button()
        auth_page.wait_changing_url_from_auth_page()
        home_page.click_personal_account_button()
        profile = personal_account_page.wait_visibility_title_profile()

        assert profile.is_displayed()

    @allure.title('Проверяем открытие истории заказов пользователя')
    @allure.description(
        'Создаём в фикстуре тестовый аккаунт, авторизуемся им в тесте и заходим в личный кабинет. Открываем историю заказов. После проверки аккаунт удаляется в фикстуре')
    def test_open_order_history(self, driver, user):
        home_page = HomePage(driver)
        personal_account_page = PersonalAccountPage(driver)
        auth_page = AuthPage(driver)
        home_page.click_login_to_account_button()
        auth_page.input_email_for_authorization()
        auth_page.input_password_for_authorization()
        auth_page.click_login_button()
        auth_page.wait_changing_url_from_auth_page()
        home_page.click_personal_account_button()
        personal_account_page.wait_visibility_title_profile()
        personal_account_page.click_order_history()
        personal_account_page.wait_changing_url_from_profile_page()
        order_history = personal_account_page.find_order_history_select()

        assert order_history.is_displayed()

    @allure.title('Проверяем выход из аккаунта')
    @allure.description(
        'Создаём в фикстуре тестовый аккаунт, авторизуемся им в тесте и заходим в личный кабинет. Затем выходим из аккаунта. После проверки аккаунт удаляется в фикстуре')
    def test_logout_from_personal_account(self, driver, user):
        home_page = HomePage(driver)
        personal_account_page = PersonalAccountPage(driver)
        auth_page = AuthPage(driver)
        home_page.click_login_to_account_button()
        auth_page.input_email_for_authorization()
        auth_page.input_password_for_authorization()
        auth_page.click_login_button()
        auth_page.wait_changing_url_from_auth_page()
        home_page.click_personal_account_button()
        personal_account_page.wait_visibility_title_profile()
        personal_account_page.click_logout_button()
        personal_account_page.wait_changing_url_from_profile_page()
        entrance = auth_page.find_login_button()

        assert entrance.is_displayed()
