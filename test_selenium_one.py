import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_all_pets(authorization):
    pytest.driver.implicitly_wait(10)
    images = pytest.driver.find_elements_by_css_selector('.card-deck .card-img-top')
    names = pytest.driver.find_elements_by_css_selector('.card-deck .card-title')
    descriptions = pytest.driver.find_elements_by_css_selector('.card-deck .card-text')

    for i in range(len(names)):
        assert images[i].get_attribute('src') != ''
        assert names[i].text != ''
        assert descriptions[i].text != ''
        assert ', ' in descriptions[i].text
        parts = descriptions[i].text.split(", ")
        assert len(parts[0]) > 0
        assert len(parts[1]) > 0


def test_my_pets(authorization):
    pytest.driver.find_element_by_xpath('//a[@href="/my_pets"]').click()
    WebDriverWait(pytest.driver, 10).until(EC.title_is(title="PetFriends: My Pets"))

    WebDriverWait(pytest.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//td[1]')))
    names = pytest.driver.find_elements_by_xpath('//td[1]')
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//th[@scope="row"]/img')))
    images = pytest.driver.find_elements_by_xpath('//th[@scope="row"]/img')
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//td[2]')))
    species = pytest.driver.find_elements_by_xpath('//td[2]')
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//td[3]')))
    ages = pytest.driver.find_elements_by_xpath('//td[3]')

    user_stats = pytest.driver.find_element_by_xpath('//div[@class=".col-sm-4 left"]').text.split('\n')
    pets_qty = user_stats[1][len('Питомцев: '):]
    pets_qty = int(pets_qty) if len(pets_qty) > 0 else 0
    assert len(names) == pets_qty

    pets_image_qty = 0
    for img in range(len(images)):
        if images[img].get_attribute("src") != "":
            pets_image_qty += 1
    assert pets_image_qty * 2 >= pets_qty

    for i in range(len(names)):
        assert names[i].text != ""
        assert ages[i].text != ""
        assert species[i].text != ""

    list_of_names = []
    for n in range(len(names)):
        if names[n].text not in list_of_names:
            list_of_names.append(names[n].text)
        else:
            assert False
