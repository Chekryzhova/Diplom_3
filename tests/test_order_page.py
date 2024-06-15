from pages.home_page import HomePage
from pages.order_page import OrderPage
from pages.auth_page import AuthPage
from pages.personal_account_page import PersonalAccountPage
import allure

class TestOrderPage:

    @allure.title('Проверка открытия информации о заказе')
    @allure.description('Переходим на страницу ленты заказов и нажимаем на первый заказ. проверяем, что открылось окно с информацией о нём')
    def test_open_order_info(self, driver):
        home_page = HomePage(driver)
        order_page = OrderPage(driver)
        home_page.click_feed_order()
        home_page.wait_order_feed_header()
        order_page.click_first_order()
        close_button = order_page.wait_close_order_info_button()

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
        auth_page.wait_changing_url_from_auth_page()
        home_page.add_ingredient_to_order()
        home_page.click_create_order_button()
        home_page.wait_close_order_popup()
        home_page.close_order_popup()
        home_page.click_personal_account_button()
        personal_account.wait_visibility_title_profile()
        personal_account.click_order_history()
        personal_account.wait_order_number()
        order_number = personal_account.get_number_order()
        home_page.click_feed_order()
        home_page.wait_order_feed_header()
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
        auth_page.wait_changing_url_from_auth_page()
        home_page.click_feed_order()
        home_page.wait_order_feed_header()
        alltime_orders_before = order_page.get_counter_orders_for_alltime()
        home_page.click_stellarburger_logo()
        home_page.add_ingredient_to_order()
        home_page.click_create_order_button()
        home_page.wait_close_order_popup()
        home_page.close_order_popup()
        home_page.click_feed_order()
        home_page.wait_order_feed_header()
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
        auth_page.wait_changing_url_from_auth_page()
        home_page.click_feed_order()
        home_page.wait_order_feed_header()
        allday_orders_before = order_page.get_counter_orders_for_allday()
        home_page.click_stellarburger_logo()
        home_page.add_ingredient_to_order()
        home_page.click_create_order_button()
        home_page.wait_close_order_popup()
        home_page.close_order_popup()
        home_page.click_feed_order()
        home_page.wait_order_feed_header()
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
        auth_page.wait_changing_url_from_auth_page()
        home_page.add_ingredient_to_order()
        home_page.click_create_order_button()
        home_page.wait_close_order_popup()
        home_page.close_order_popup()
        home_page.click_personal_account_button()
        personal_account.wait_visibility_title_profile()
        personal_account.click_order_history()
        personal_account.wait_order_number()
        order_number = personal_account.get_number_order()
        home_page.click_feed_order()
        home_page.wait_order_feed_header()
        order_page.wait_invisibility_no_orders_in_work()
        order_in_work = order_page.get_orders_in_work()

        assert order_number in order_in_work














