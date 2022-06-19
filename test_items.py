from selenium import webdriver
from selenium.webdriver.common.by import By
import time



link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def is_element_present(browser):
    try:
        browser.get(link)
        time.sleep(10)
        browser.implicitly_wait(10)
        browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket")
        return True
    except:
        return False

def test_basket(browser):

    assert is_element_present(browser) == True, 'button not found'