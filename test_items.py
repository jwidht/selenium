import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

link="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

# @pytest.mark.parametrize('language', ["ru", "en"])
def test_btn_present(browser):
    browser.get(link)
    time.sleep(5) 
    btn = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "button.btn-add-to-basket"))
    )
    print( "method 1 finished")
    #button = browser.find_element(By.ID, "btn btn-lg btn-primary ")
    #button.click()
    assert browser.find_elements(By.CSS_SELECTOR, 'button.btn-add-to-basket'), "Second way to test presence failed"
    print( "method 2 finished")

def test_btn_not_present1(browser):
    browser.get(link)
    btn = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input.btn-add-to-basket"))
    )
    print( "not present: method 1 finished")

def test_btn_not_present2(browser):
    browser.get(link)
    assert browser.find_elements(By.CSS_SELECTOR, 'input.btn-add-to-basket'), "Second way to test NO presence failed"
    print( "not present: method 2 finished")
