from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import math
import time
from selenium.webdriver.support.ui import Select


def sum_value1_value2(x,y):
    return (x+y)


try:
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element_by_id ("num1")
    value1 = int(x.text)

    y = browser.find_element_by_id("num2")
    value2 = int(y.text)

    sum1 = sum_value1_value2(value1, value2)
    print (sum1)
    time.sleep(1)

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value (str(sum1))
    time.sleep(1)


    button = browser.find_element_by_css_selector(".btn-default")
    button.click()

    time.sleep(10)



finally:
    time.sleep(1)
    browser.quit()


#