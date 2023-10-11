from . import webdriver, By, Keys, Select, EC, ChromeService, ChromeDriverManager, WebDriverWait, pytest



def wait_for_clickable(driver, timeout, locator):
    WebDriverWait(driver, timeout).until(EC.element_to_be_clickable(locator),
                                    "Element not clicable")




def wait_to_be_visible(driver, timeout, locator):
    element = WebDriverWait(driver, timeout).until(EC.visibility_of_element_located(locator),
                                    "Element not visible")
    return element



@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()






def add_cookie(driver, name, value):
    driver.add_cookie({'name': name, 'value': value})
    driver.refresh()



def delete_cookies(driver):
    driver.delete_cookies()
    driver.refresh()



def assert_text_in_element(driver, locator, expected_result):
    element = driver.find_element(By.XPATH, locator)
    assert element.text == expected_result, "Text not the same"


def assert_value_in_element_attribute(driver, locator, attribute, expected_result):
    element = driver.find_element(By.XPATH, locator)
    value = element.get_attribute(attribute)
    assert value == expected_result, "Attribute value not the same"


def hard_click(driver, locator):
    element = driver.find_element(By.XPATH, locator)
    driver.execute_script("arguments[0].click();", element)


def fill(driver, locator, text):
    element = driver.find_element(By.XPATH, locator)
    element.clear()
    element.sendKeys(text)
    element.sendKeys('')


def converter_of_name(button_name):
    button_name = button_name.lower().strip()
    if (button_name == 'wszystkie' or button_name =='nowe' or button_name =='hybrydowe'
            or button_name =='elektryczne' or button_name =='miejskie' or button_name =='rodzinne'):
        button_name = button_name.capitalize()
    elif button_name == 'suv/crossover':
        result = ''
        for index, char in enumerate(button_name):
            if index in [0, 1, 2, 4]:
                result += char.upper()
            else:
                result += char
        button_name = result
    return button_name





def car_class_converter(car, class_of_car_name):
    class_of_car_name = class_of_car_name.replace('_', ' ')
    class_of_car_name = class_of_car_name.upper()
    class_of_car_name = class_of_car_name.strip()
    car_tag_for_search = car[class_of_car_name]
    return car_tag_for_search


