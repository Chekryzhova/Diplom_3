import requests
import allure

class StellarBurgersApi:

    @staticmethod
    def create_user(body):
        with allure.step('Создаём юзера'):
            return requests.post("https://stellarburgers.nomoreparties.site/api/auth/register", json=body)

    @staticmethod
    def delete_user(access):
        with allure.step('Удаляем юзера'):
            return requests.delete("https://stellarburgers.nomoreparties.site/api/auth/user", headers={"Authorization": access})