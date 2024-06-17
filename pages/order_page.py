from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
import allure

class OrderPage(BasePage):

    @allure.step('Жмём на первый заказ в ленте заказов')
    def click_first_order(self):
        self.click_element(OrderPageLocators.FIRST_ORDER)

    @allure.step('Ждём кнопку, закрывающую информацию о заказе')
    def wait_close_order_info_button(self):
        return self.wait_visibility_of_element_located(OrderPageLocators.CLOSE_ORDER_INFO_BUTTON)

    @allure.step('Получаем весь список заказов')
    def get_order_list(self):
        return self.find_element(OrderPageLocators.ORDER_LIST).text


    @allure.step('Получаем количество заказов за всё время')
    def get_counter_orders_for_alltime(self):
        alltime_orders = self.find_element(OrderPageLocators.COUNTER_ORDERS_FOR_ALLTIME).text
        return alltime_orders

    @allure.step('Получаем количество заказов за весь день')
    def get_counter_orders_for_allday(self):
        allday_orders = self.find_element(OrderPageLocators.COUNTER_ORDERS_FOR_ALLDAY).text
        return allday_orders

    @allure.step('Получаем заказы в работе')
    def get_orders_in_work(self):
        order_in_work = self.find_element(OrderPageLocators.ORDER_IN_WORK).text
        return order_in_work

    @allure.step('Ждём, когда надпись все текущие заказы готовы исчезнет')
    def wait_invisibility_no_orders_in_work(self):
        self.wait_invisibility_of_element_located(OrderPageLocators.NO_ORDERS_IN_WORK)

    @allure.step('Ждём надпись лента заказов')
    def wait_order_feed_header(self):
        return self.wait_visibility_of_element_located(OrderPageLocators.ORDER_FEED_HEADING)


