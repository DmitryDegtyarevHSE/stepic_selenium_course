from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time
import os


try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)
    inputs = browser.find_elements(By.TAG_NAME, "input")
    for i in range(len(inputs)-1):
        inputs[i].send_keys("Puta")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'ssjj.txt')
    inputs[-1].send_keys(file_path)

    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

finally:
    time.sleep(10)
    browser.quit()