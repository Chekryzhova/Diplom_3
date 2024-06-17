import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from seletools.actions import drag_and_drop


class BasePage:
    @allure.step('Инициализируем драйвер')
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Базовый метод поиска элемента')
    def find_element(self, locator):
        return self.driver.find_element(*locator)

    @allure.step('Базовый метод клика по элементу')
    def click_element(self, locator):
        button = self.find_element(locator)
        self.driver.execute_script("arguments[0].click();", button)

    @allure.step('Базовый метод ввода информации в поле')
    def input(self, locator, text):
        imput_data = self.find_element(locator)
        imput_data.send_keys(text)

    @allure.step('Базовый метод ожидания, что элемент станет кликабельным')
    def wait_element_to_be_clickable(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))

    @allure.step('Базовый метод ожидания, что элемент станет видимым')
    def wait_visibility_of_element_located(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))

    @allure.step('Базовый метод ожидания, что элемент станет невидимым')
    def wait_invisibility_of_element_located(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located(locator))

    @allure.step('Базовый метод ожидания изменения урла')
    def wait_change_url(self, url):
        return WebDriverWait(self.driver, 10).until(EC.url_changes(url))

    @allure.step('Базовый метод перетаскивания элемента')
    def drag_and_drop(self, sourse, target):
        drag_and_drop(self.driver, sourse, target)



