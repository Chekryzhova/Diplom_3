import urls
from selenium import webdriver
import pytest
from data import StellarBurgerData
from helper import StellarBurgersApi


@pytest.fixture(params=['firefox', 'chrome'])
def driver(request):
    browser = None

    if request.param == 'firefox':
        browser = webdriver.Firefox()
        browser.maximize_window()
    elif request.param == 'chrome':
        browser = webdriver.Chrome()
        browser.maximize_window()

    browser.get(urls.BURGER)

    yield browser

    browser.quit()

@pytest.fixture(scope='function')
def user():
    create_user_requests = StellarBurgersApi.create_user(StellarBurgerData.CREATE_USER_BODY)
    access = create_user_requests.json()["accessToken"]

    yield create_user_requests

    StellarBurgersApi.delete_user(access)


