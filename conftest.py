import pytest
from selenium import webdriver


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture(autouse=True)
def setup_selenium():
    pytest.driver = webdriver.Chrome("C:\\chromedriver.exe")
    pytest.driver.set_window_size(1600, 1000)
    yield
    pytest.driver.quit()


@pytest.fixture()
def authorization():
    pytest.driver.get('http://petfriends1.herokuapp.com/login')
    pytest.driver.find_element_by_id('email').send_keys('pepatest@gmail.com')
    pytest.driver.find_element_by_id('pass').send_keys('12345')
    pytest.driver.find_element_by_css_selector('button[type="submit"]').click()
    yield pytest.driver
