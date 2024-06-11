import allure


class BasePage:
    @allure.step('Инициализируем драйвер')
    def __init__(self, driver):
        self.driver = driver
