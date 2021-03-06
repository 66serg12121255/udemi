

def calc(x):
    return  str(math.log(abs(12 * math.sin(x))))


try:
    browser = webdriver.Chrome()

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    w = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )

    button = browser.find_element_by_id("book")
    button.click()

    x_element = browser.find_element_by_id ('input_value')
    x = int(x_element.text)
    y = calc(x)

    input1 = browser.find_element_by_id('answer')
    input1.send_keys(y)

    button = browser.find_element_by_id("solve")
    button.click()


finally:
    time.sleep(4)
    browser.quit()
