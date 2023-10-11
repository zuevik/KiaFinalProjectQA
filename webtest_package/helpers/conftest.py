import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType


@pytest.fixture(autouse=False)
def browser_chrome():
    print("-------")
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(5)

    yield driver

    driver.close()
    driver.quit()

    print("+++++++++")

#
# @pytest.fixture(autouse=False)
# def browser_firefox():
#     driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
#     driver.implicitly_wait(5)
#
#     yield driver
#
#     driver.close()
#     driver.quit()