from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.home_page import HomePage
from pages.order_page import OrderPage
from pages.auth_page import AuthPage
from pages.personal_account_page import PersonalAccountPage
from locators.order_page_locators import OrderPageLocators
from locators.home_page_locators import HomePageLocators
from locators.personal_account_page_locators import PersovalAccountPageLocators
import allure

class TestOrderPage:

    @allure.title('Проверка открытия информации о заказе')
    @allure.description('Переходим на страницу ленты заказов и нажимаем на первый заказ. проверяем, что открылось окно с информацией о нём')
    def test_open_order_info(self, driver):
        home_page = HomePage(driver)
        order_page = OrderPage(driver)
        home_page.click_feed_order()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(OrderPageLocators.ORDER_FEED_HEADING))
        order_page.click_first_order()
        close_button = (WebDriverWait(driver, 10).until(EC.visibility_of_element_located(OrderPageLocators.CLOSE_ORDER_INFO_BUTTON)))

        assert close_button.is_displayed()

    @allure.title('Проверка того, что заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    @allure.description(
        'Создаём в фикстуре тестовый аккаунт, авторизуемся им в тесте, создаём заказ и проверяем, что этот заказ есть в истории заказов и в ленте заказов. После проверки аккаунт удаляется в фикстуре')
    def test_order_in_orderlist_and_orderhistory(self, driver, user):
        home_page = HomePage(driver)
        auth_page = AuthPage(driver)
        order_page = OrderPage(driver)
        personal_account = PersonalAccountPage(driver)
        home_page.click_login_to_account_button()
        auth_page.input_email_for_authorization()
        auth_page.input_password_for_authorization()
        auth_page.click_login_button()
        WebDriverWait(driver, 10).until(EC.url_changes('https://stellarburgers.nomoreparties.site/login'))
        home_page.add_ingredient_to_order()
        home_page.click_create_order_button()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(HomePageLocators.CLOSE_ORDER_POPUP))
        home_page.close_order_popup()
        home_page.click_personal_account_button()
        WebDriverWait(driver, 15).until(EC.visibility_of_element_located(PersovalAccountPageLocators.TITLE_PROFILE))
        personal_account.click_order_history()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(PersovalAccountPageLocators.ORDER_NUMBER))
        order_number = personal_account.get_number_order()
        home_page.click_feed_order()
        WebDriverWait(driver, 25).until(EC.visibility_of_element_located(OrderPageLocators.ORDER_FEED_HEADING))
        order_list = order_page.get_order_list()

        assert order_number in order_list

    @allure.title('Проверка того, что при создании нового заказа счётчик "Выполнено за всё время" увеличивается')
    @allure.description(
        'Создаём в фикстуре тестовый аккаунт, авторизуемся им в тесте, проверяем цифру созданных за всё время заказов. создаём заказ и проверяем, что счётчик "Выполнено за всё время" увеличился. После проверки аккаунт удаляется в фикстуре')
    def test_counter_orders_for_alltime(self, driver, user):
        home_page = HomePage(driver)
        auth_page = AuthPage(driver)
        order_page = OrderPage(driver)
        home_page.click_login_to_account_button()
        auth_page.input_email_for_authorization()
        auth_page.input_password_for_authorization()
        auth_page.click_login_button()
        WebDriverWait(driver, 10).until(EC.url_changes('https://stellarburgers.nomoreparties.site/login'))
        home_page.click_feed_order()
        WebDriverWait(driver, 25).until(EC.visibility_of_element_located(OrderPageLocators.ORDER_FEED_HEADING))
        alltime_orders_before = order_page.get_counter_orders_for_alltime()
        home_page.click_stellarburger_logo()
        home_page.add_ingredient_to_order()
        home_page.click_create_order_button()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(HomePageLocators.CLOSE_ORDER_POPUP))
        home_page.close_order_popup()
        home_page.click_feed_order()
        WebDriverWait(driver, 25).until(EC.visibility_of_element_located(OrderPageLocators.ORDER_FEED_HEADING))
        alltime_orders_after = order_page.get_counter_orders_for_alltime()

        assert alltime_orders_before < alltime_orders_after

    @allure.title('Проверка того, что при создании нового заказа счётчик "Выполнено за сегодня" увеличивается')
    @allure.description(
        'Создаём в фикстуре тестовый аккаунт, авторизуемся им в тесте, проверяем цифру созданных за сегодня заказов. создаём заказ и проверяем, что счётчик "Выполнено за сегодня" увеличился. После проверки аккаунт удаляется в фикстуре')
    def test_counter_orders_for_allday(self, driver, user):
        home_page = HomePage(driver)
        auth_page = AuthPage(driver)
        order_page = OrderPage(driver)
        home_page.click_login_to_account_button()
        auth_page.input_email_for_authorization()
        auth_page.input_password_for_authorization()
        auth_page.click_login_button()
        WebDriverWait(driver, 10).until(EC.url_changes('https://stellarburgers.nomoreparties.site/login'))
        home_page.click_feed_order()
        WebDriverWait(driver, 25).until(EC.visibility_of_element_located(OrderPageLocators.ORDER_FEED_HEADING))
        allday_orders_before = order_page.get_counter_orders_for_allday()
        home_page.click_stellarburger_logo()
        home_page.add_ingredient_to_order()
        home_page.click_create_order_button()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(HomePageLocators.CLOSE_ORDER_POPUP))
        home_page.close_order_popup()
        home_page.click_feed_order()
        WebDriverWait(driver, 25).until(EC.visibility_of_element_located(OrderPageLocators.ORDER_FEED_HEADING))
        allday_orders_after = order_page.get_counter_orders_for_allday()

        assert allday_orders_before < allday_orders_after

    @allure.title('Проверка того, что после оформления заказа его номер появляется в разделе В работе')
    @allure.description(
        'Создаём в фикстуре тестовый аккаунт, авторизуемся им в тесте, создаём заказ и проверяем, что этот заказ появился в рзделе "В работе". После проверки аккаунт удаляется в фикстуре')
    def test_order_in_work(self, driver, user):
        home_page = HomePage(driver)
        auth_page = AuthPage(driver)
        order_page = OrderPage(driver)
        personal_account = PersonalAccountPage(driver)
        home_page.click_login_to_account_button()
        auth_page.input_email_for_authorization()
        auth_page.input_password_for_authorization()
        auth_page.click_login_button()
        WebDriverWait(driver, 10).until(EC.url_changes('https://stellarburgers.nomoreparties.site/login'))
        home_page.add_ingredient_to_order()
        home_page.click_create_order_button()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(HomePageLocators.CLOSE_ORDER_POPUP))
        home_page.close_order_popup()
        home_page.click_personal_account_button()
        WebDriverWait(driver, 15).until(EC.visibility_of_element_located(PersovalAccountPageLocators.TITLE_PROFILE))
        personal_account.click_order_history()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(PersovalAccountPageLocators.ORDER_NUMBER))
        order_number = personal_account.get_number_order()
        home_page.click_feed_order()
        WebDriverWait(driver, 25).until(EC.visibility_of_element_located(OrderPageLocators.ORDER_FEED_HEADING))
        WebDriverWait(driver, 25).until(EC.invisibility_of_element_located(OrderPageLocators.NO_ORDERS_IN_WORK))
        order_in_work = order_page.get_orders_in_work()

        assert order_number in order_in_work














