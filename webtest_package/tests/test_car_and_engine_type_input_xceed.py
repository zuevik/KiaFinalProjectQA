from . import (By, wait_to_be_visible, Select, time, driver,
               HomePage, configurationPage, converter_of_name, carConfigPage, xceed)

def test_configuration_button_test(driver):


    home_page = HomePage(driver)
    conf_page = configurationPage(driver)
    car_config_page = carConfigPage(driver)

    home_page.open()
    home_page.cookies_button_accept()
    home_page.configurator_button_click()
    conf_page.select_car_type_and_click('nowe')
    conf_page.car_model_click('XCeed')
    time.sleep(3)
    car_config_page.choose_the_engine_click(xceed, 'M', 1.5, 'Automatyczna')
    car_type_text = car_config_page.car_type_check_test('M')
    engine_type_text = car_config_page.engine_type_check_test(1.5)
    expected_car_type = 'M'
    expected_engine_type = '1.5 T-GDI 160KM 7DCT (Benzynowy, Automatyczna DCT);'
    assert expected_car_type == car_type_text
    assert expected_engine_type == engine_type_text