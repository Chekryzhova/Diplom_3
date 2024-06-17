from pages.base_page import BasePage
from locators.home_page_locators import HomePageLocators
import allure


class HomePage(BasePage):

    @allure.step('Жмём на кнопку "Войти в аккаунт"')
    def click_login_to_account_button(self):
        self.click_element(HomePageLocators.LOGIN_TO_ACCOUNT_BUTTON)

    @allure.step('Жмём на кнопку "Личный кабинет"')
    def click_personal_account_button(self):
        self.click_element(HomePageLocators.PERSONAL_ACCOUNT_BUTTON)

    @allure.step('Жмём на кнопку конструктора')
    def click_constructor(self):
        self.click_element(HomePageLocators.CONSTRUCTOR_BUTTON)

    @allure.step('Жмём на кнопку ленты заказов')
    def click_feed_order(self):
        self.click_element(HomePageLocators.ORDER_FEED_BUTTON)

    @allure.step('Находим надпись собери бургер')
    def find_assemble_burger_text(self):
        return self.find_element(HomePageLocators.CONSTRUCTOR)


    @allure.step('Открываем окно с деталями ингредиента')
    def click_ingredient(self):
        self.click_element(HomePageLocators.FLUORESCENT_BUN)

    @allure.step('Закрываем окно с деталями ингредиента')
    def close_ingredient_info(self):
        self.click_element(HomePageLocators.CLOSE_INGREDIENT_INFO_BUTTON)

    @allure.step('Ждём кнопку, закрывающую информацию об ингредиенте')
    def wait_close_ingredient_info(self):
        return self.wait_visibility_of_element_located(HomePageLocators.CLOSE_INGREDIENT_INFO_BUTTON)


    @allure.step('Добавляем ингредиент в заказ')
    def add_ingredient_to_order(self):
        sourse = self.find_element(HomePageLocators.FLUORESCENT_BUN)
        target = self.find_element(HomePageLocators.ADD_INGREDIENT_TO_ORDER)
        self.drag_and_drop(sourse, target)

    @allure.step('Находим счётчик ингредиента')
    def find_ingredient_counter(self):
        return self.find_element(HomePageLocators.INGREDIENT_COUNTER)

    @allure.step('Жмём на кнопку создания заказа')
    def click_create_order_button(self):
        self.click_element(HomePageLocators.PLACE_ORDER_BUTTON)

    @allure.step('Жмём на кнопку закрытия заказа')
    def wait_close_order_popup(self):
        self.wait_visibility_of_element_located(HomePageLocators.CLOSE_ORDER_POPUP)

    @allure.step('Закрываем окно с созданным заказом')
    def close_order_popup(self):
        self.click_element(HomePageLocators.CLOSE_ORDER_POPUP)

    @allure.step('Нажимаем на логотип stellarburgers')
    def click_stellarburger_logo(self):
        self.click_element(HomePageLocators.LOGO_BUTTON)

    @allure.step('Ждём появления айди заказа')
    def wait_order_id(self):
        return self.wait_visibility_of_element_located(HomePageLocators.ORDER_ID)










