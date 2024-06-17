from pages.home_page import HomePage
from pages.auth_page import AuthPage
from pages.order_page import OrderPage
import allure


class TestHomePage:

    @allure.title('Проверка перехода на страницу восстановления пароля')
    @allure.description('Нажимаем на кнопку войти в аккаунт и далее переходим на страницу восстановления пароля')
    def test_go_login_recovery_page(self, driver):
        home_page = HomePage(driver)
        auth_page = AuthPage(driver)
        home_page.click_login_to_account_button()
        auth_page.click_recovery_password_button()
        recovery_button = auth_page.find_recovery_button()

        assert recovery_button.is_displayed()

    @allure.title('Проверка перехода на страницу конструктора')
    @allure.description('Нажимаем на кнопку ленты заказов, а затем нажимаем на кнопку конструктор')
    def test_click_constructor(self, driver):
        home_page = HomePage(driver)
        home_page.click_feed_order()
        home_page.click_constructor()
        constructor = home_page.find_assemble_burger_text()

        assert constructor.is_displayed()

    @allure.title('Проверка перехода на страницу ленты заказов')
    @allure.description('Нажимаем на кнопку "Лента заказов" на главной странице и проверяем, что открылась лента заказов')
    def test_click_feed_order(self, driver):
        home_page = HomePage(driver)
        order_page = OrderPage(driver)
        home_page.click_feed_order()
        feed = order_page.wait_order_feed_header()

        assert feed.is_displayed()

    @allure.title('Проверка открытия деталей ингредиента')
    @allure.description('Открываем детали ингредиента "Флюоресцентная булка R2-D3" на главной странице')
    def test_click_ingredient(self, driver):
        home_page = HomePage(driver)
        home_page.click_ingredient()
        popup_ingredient = home_page.wait_close_ingredient_info()

        assert popup_ingredient.is_displayed()

    @allure.title('Проверка закрытия деталей ингредиента')
    @allure.description('Открываем детали ингредиента "Флюоресцентная булка R2-D3" на главной странице, а затем проверяем, что всплывающее окно с деталями ингредиента закрывается')
    def test_close_ingredient_info(self, driver):
        home_page = HomePage(driver)
        home_page.click_ingredient()
        home_page.wait_close_ingredient_info()
        home_page.close_ingredient_info()
        close_popup = home_page.find_assemble_burger_text()

        assert close_popup.is_displayed()

    @allure.title('Проверка, что при добавлении ингредиента в заказ счётчик этого ингридиента увеличивается')
    @allure.description('Добавляем в заказ ингредиент "Флюоресцентная булка R2-D3" и проверяем, что его счётчик стал равен 2')
    def test_increasing_ingredient_counter(self, driver):
        home_page = HomePage(driver)
        home_page.add_ingredient_to_order()
        increasing_ingredient = home_page.find_ingredient_counter()

        assert increasing_ingredient.is_displayed()

    @allure.title('Проверка, что залогиненный пользователь может оформить заказ')
    @allure.description('Создаём в фикстуре тестовый аккаунт, авторизуемся им в тесте, добавляем в заказ ингредиент "Флюоресцентная булка R2-D3" и нажимаем на кнопку оформления заказа. Проверяем, что заказ создался. После проверки аккаунт удаляется в фикстуре')
    def test_create_order_logged_user(self, driver, user):
        home_page = HomePage(driver)
        auth_page = AuthPage(driver)
        home_page.click_login_to_account_button()
        auth_page.input_email_for_authorization()
        auth_page.input_password_for_authorization()
        auth_page.click_login_button()
        auth_page.wait_changing_url_from_auth_page()
        home_page.add_ingredient_to_order()
        home_page.click_create_order_button()
        order_id = home_page.wait_order_id()

        assert order_id.is_displayed()










