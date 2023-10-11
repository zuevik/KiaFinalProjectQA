from . import (By, wait_to_be_visible, Select, time, driver, car_class_converter)

class carConfigPage:
    def __init__(self, driver):
        self.driver = driver


    def choose_the_engine_click(self, car, car_class, engine_volume, gearbox_type):
        car_tag_for_search = car_class_converter(car, car_class)
        self.driver.find_element(By.XPATH, f'//label[contains(@for, "{car_tag_for_search}") and contains(text(), "{engine_volume}") and contains(text(), "{gearbox_type}")]').click()

    def next_button(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH, '//div[@class="btn_area btns_navigation desk"]/a[@class="direction_btn eut_cmpe_btn" and contains(text(), "Dalej")]').click()
        time.sleep(3)


    def choose_the_car_color(self, color_number):
        self.driver.find_element(By.XPATH,f'//*[@id="exterior_color"]/div[2]/div/ul/li[{color_number}]').click()


    def car_type_check_test(self, car_type_to_check):
        time.sleep(2)
        car_type_check = wait_to_be_visible(self.driver, 5, (By.XPATH, f'//*[@id="contents"]//strong[contains(text(), "{car_type_to_check}")]'))
        car_type_text = car_type_check.text
        return car_type_text

    def engine_type_check_test(self, engine_type_to_check):
        time.sleep(2)
        engine_type_check = wait_to_be_visible(self.driver, 5, (By.XPATH, f'//*[@id="contents"]//span[contains(text(), "{engine_type_to_check}")]'))
        engine_type_text = engine_type_check.text
        return engine_type_text