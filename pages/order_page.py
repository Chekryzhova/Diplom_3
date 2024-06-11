from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
import allure

class OrderPage(BasePage):

    @allure.step('Жмём на первый заказ в ленте заказов')
    def click_first_order(self):
        first_order = self.driver.find_element(*OrderPageLocators.FIRST_ORDER)
        self.driver.execute_script("arguments[0].click();", first_order)

    @allure.step('Получаем весь список заказов')
    def get_order_list(self):
        feed_order = self.driver.find_element(*OrderPageLocators.ORDER_LIST).text
        return feed_order

    @allure.step('Получаем количество заказов за всё время')
    def get_counter_orders_for_alltime(self):
        alltime_orders = self.driver.find_element(*OrderPageLocators.COUNTER_ORDERS_FOR_ALLTIME).text
        return alltime_orders

    @allure.step('Получаем количество заказов за весь день')
    def get_counter_orders_for_allday(self):
        allday_orders = self.driver.find_element(*OrderPageLocators.COUNTER_ORDERS_FOR_ALLDAY).text
        return allday_orders

    @allure.step('Получаем заказы в работе')
    def get_orders_in_work(self):
        order_in_work = self.driver.find_element(*OrderPageLocators.ORDER_IN_WORK).text
        return order_in_work


