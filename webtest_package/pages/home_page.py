from . import By, wait_to_be_visible, Select, time, driver


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get('https://www.kia.com/pl/')
        time.sleep(5)

    def cookies_button_accept(self):
        wait_to_be_visible(self.driver, 7, (By.ID, 'onetrust-accept-btn-handler')).click()
        time.sleep(3)

    def configurator_button_click(self):
        wait_to_be_visible(self.driver, 10, (By.XPATH,
        '//*[@id="eut_gnb"]/li[9]/a/span')).click()
        time.sleep(15)













