from pages.base_page import BasePage
from locators.personal_account_page_locators import PersovalAccountPageLocators
import allure
import urls

class PersonalAccountPage(BasePage):

    @allure.step('Жмём на историю заказов в личном кабинете')
    def click_order_history(self):
        self.click_element(PersovalAccountPageLocators.ORDER_HISTORY)


    @allure.step('Жмём на кнопку выхода в личном кабинете')
    def click_logout_button(self):
        self.click_element(PersovalAccountPageLocators.LOGOUT_BUTTON)


    @allure.step('Получаем номер созданного перед этим заказа')
    def get_number_order(self):
        order_number = self.find_element(PersovalAccountPageLocators.ORDER_NUMBER).text
        return order_number.replace('#', '')

    @allure.step('Жмём видимости поля Профиль')
    def wait_visibility_title_profile(self):
        return self.wait_visibility_of_element_located(PersovalAccountPageLocators.TITLE_PROFILE)

    @allure.step('Жмём перехода со страницы профиля')
    def wait_changing_url_from_profile_page(self):
        self.wait_change_url(urls.BURGER + urls.PROFILE)

    @allure.step('Жмём, что "История заказов" будет выделена')
    def find_order_history_select(self):
        return self.find_element(PersovalAccountPageLocators.ORDER_HISTORY_SELECT)

    @allure.step('Жмём видимости номера заказа')
    def wait_order_number(self):
        self.wait_visibility_of_element_located(PersovalAccountPageLocators.ORDER_NUMBER)
