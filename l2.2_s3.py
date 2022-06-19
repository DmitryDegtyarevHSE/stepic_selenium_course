from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = int(browser.find_element(By.ID, "num1").text)
    num2 = int(browser.find_element(By.ID, "num2").text)
    res = num1+num2

    sel = Select(browser.find_element(By.TAG_NAME, "select"))
    sel.select_by_value(f"{str(res)}")

    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

finally:

    time.sleep(10)
    browser.quit()
