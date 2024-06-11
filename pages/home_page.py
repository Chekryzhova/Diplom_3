from pages.base_page import BasePage
from locators.home_page_locators import HomePageLocators
from seletools.actions import drag_and_drop
import allure


class HomePage(BasePage):

    @allure.step('Жмём на кнопку "Войти в аккаунт"')
    def click_login_to_account_button(self):
        auth_button = self.driver.find_element(*HomePageLocators.LOGIN_TO_ACCOUNT_BUTTON)
        self.driver.execute_script("arguments[0].click();", auth_button)

    @allure.step('Жмём на кнопку "Личный кабинет"')
    def click_personal_account_button(self):
        personal_account_button = self.driver.find_element(*HomePageLocators.PERSONAL_ACCOUNT_BUTTON)
        self.driver.execute_script("arguments[0].click();", personal_account_button)

    @allure.step('Жмём на кнопку конструктора')
    def click_constructor(self):
        constructor_button = self.driver.find_element(*HomePageLocators.CONSTRUCTOR_BUTTON)
        self.driver.execute_script("arguments[0].click();", constructor_button)

    @allure.step('Жмём на кнопку ленты заказов')
    def click_feed_order(self):
        feed_order_button = self.driver.find_element(*HomePageLocators.ORDER_FEED_BUTTON)
        self.driver.execute_script("arguments[0].click();", feed_order_button)

    @allure.step('Открываем окно с деталями ингредиента')
    def click_ingredient(self):
        ingredient = self.driver.find_element(*HomePageLocators.FLUORESCENT_BUN)
        self.driver.execute_script("arguments[0].click();", ingredient)

    @allure.step('Закрываем окно с деталями ингредиента')
    def close_ingredient_info(self):
        close_button = self.driver.find_element(*HomePageLocators.CLOSE_INGREDIENT_INFO_BUTTON)
        self.driver.execute_script("arguments[0].click();", close_button)

    @allure.step('Добавляем ингредиент в заказ')
    def add_ingredient_to_order(self):
        sourse = self.driver.find_element(*HomePageLocators.FLUORESCENT_BUN)
        target = self.driver.find_element(*HomePageLocators.ADD_INGREDIENT_TO_ORDER)
        drag_and_drop(self.driver, sourse, target)

    @allure.step('Жмём на кнопку создания заказа')
    def click_create_order_button(self):
        order_button = self.driver.find_element(*HomePageLocators.PLACE_ORDER_BUTTON)
        self.driver.execute_script("arguments[0].click();", order_button)

    @allure.step('Закрываем окно с созданным заказом')
    def close_order_popup(self):
        close_order = self.driver.find_element(*HomePageLocators.CLOSE_ORDER_POPUP)
        self.driver.execute_script("arguments[0].click();", close_order)

    @allure.step('Нажимаем на логотип stellarburgers')
    def click_stellarburger_logo(self):
        logo = self.driver.find_element(*HomePageLocators.LOGO_BUTTON)
        self.driver.execute_script("arguments[0].click();", logo)









