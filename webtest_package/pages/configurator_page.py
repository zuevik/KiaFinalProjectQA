from . import By, wait_to_be_visible, Select, time, driver, converter_of_name


class configurationPage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get('https://www.kia.com/pl/sprzedaz/konfigurator/#/CarSelector')
        time.sleep(5)



    def select_car_type_and_click(self, input_category):
        button_name = converter_of_name(input_category)
        wait_to_be_visible(self.driver, 15, (By.XPATH, f'//label[text()="{button_name}"]')).click()


    def car_model_click(self, car_model):
        self.driver.find_element(By.XPATH, f'//ul[@id="eut-ms1"]//h3[text()="{car_model}"]').click()
        time.sleep(5)



























