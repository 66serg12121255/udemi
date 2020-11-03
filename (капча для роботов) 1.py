from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import math
import time

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))



try:
    link = " http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)


    x_element = browser.find_element_by_id ('input_value')
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element_by_id('answer')
    input1.send_keys(y)

    option1 = browser.find_element_by_id("robotCheckbox")
    option1.click()

    # option1 = browser.find_element_by_id("robotsRule")
    # option1.click()

    time.sleep(1)

    option1 = browser.find_element_by_css_selector("[for='robotsRule']")
    option1.click()


    button = browser.find_element_by_css_selector(".btn-default")
    button.click()


    time.sleep(5)

finally:
    time.sleep(1)
    browser.quit()