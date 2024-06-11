from pages.base_page import BasePage
from locators.personal_account_page_locators import PersovalAccountPageLocators
import allure
class PersonalAccountPage(BasePage):

    @allure.step('Жмём на историю заказов в личном кабинете')
    def click_order_history(self):
        order_history_button = self.driver.find_element(*PersovalAccountPageLocators.ORDER_HISTORY)
        self.driver.execute_script("arguments[0].click();", order_history_button)

    @allure.step('Жмём на кнопку выхода в личном кабинете')
    def click_logout_button(self):
        logout_button = self.driver.find_element(*PersovalAccountPageLocators.LOGOUT_BUTTON)
        self.driver.execute_script("arguments[0].click();", logout_button)

    @allure.step('Получаем номер созданного перед этим заказа')
    def get_number_order(self):
        order_number = self.driver.find_element(*PersovalAccountPageLocators.ORDER_NUMBER).text
        return order_number.replace('#', '')
