from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.home_page import HomePage
from pages.auth_page import AuthPage
from pages.personal_account_page import PersonalAccountPage
from locators.personal_account_page_locators import PersovalAccountPageLocators
from locators.auth_page_locators import AuthPageLocators
from selenium.webdriver.common.by import By
import allure


class TestPersonalAccount:

    @allure.title('Проверяем открытие личного кабинета')
    @allure.description('Создаём в фикстуре тестовый аккаунт, авторизуемся им в тесте и заходим в личный кабинет. После проверки аккаунт удаляется в фикстуре')
    def test_open_personal_account(self, user, driver):
        home_page = HomePage(driver)
        auth_page = AuthPage(driver)
        home_page.click_login_to_account_button()
        auth_page.input_email_for_authorization()
        auth_page.input_password_for_authorization()
        auth_page.click_login_button()
        WebDriverWait(driver, 10).until(EC.url_changes('https://stellarburgers.nomoreparties.site/login'))
        home_page.click_personal_account_button()
        profile = (WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located(PersovalAccountPageLocators.TITLE_PROFILE)))

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
        WebDriverWait(driver, 10).until(EC.url_changes('https://stellarburgers.nomoreparties.site/login'))
        home_page.click_personal_account_button()
        WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located(PersovalAccountPageLocators.ORDER_HISTORY))
        personal_account_page.click_order_history()
        WebDriverWait(driver, 10).until(EC.url_changes('https://stellarburgers.nomoreparties.site/account/profile'))
        order_history = driver.find_element(By.XPATH, "//a[contains(@class, 'Account_link_active__2opc9')]")

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
        WebDriverWait(driver, 10).until(EC.url_changes('https://stellarburgers.nomoreparties.site/login'))
        home_page.click_personal_account_button()
        WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located(PersovalAccountPageLocators.ORDER_HISTORY))
        personal_account_page.click_logout_button()
        WebDriverWait(driver, 10).until(EC.url_changes('https://stellarburgers.nomoreparties.site/account/profile'))
        entrance = driver.find_element(*AuthPageLocators.LOGIN_BUTTON)

        assert entrance.is_displayed()
