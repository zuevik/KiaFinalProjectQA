from . import (By, wait_to_be_visible, Select, time, driver,
               HomePage, configurationPage, converter_of_name, carConfigPage,ceed)

def test_configuration_button_test(driver):


    home_page = HomePage(driver)
    conf_page = configurationPage(driver)
    car_config_page = carConfigPage(driver)

    home_page.open()
    home_page.cookies_button_accept()
    home_page.configurator_button_click()
    conf_page.select_car_type_and_click('miejskie')
    conf_page.car_model_click('Ceed')
    time.sleep(3)
    car_config_page.choose_the_engine_click(ceed , 'GTL', 1.5, 'Automatyczna')
    car_type_text = car_config_page.car_type_check_test('GT')
    engine_type_text = car_config_page.engine_type_check_test(1.5)
    expected_car_type = 'GT Line'
    expected_engine_type = '1.5 T-GDI 160KM 7DCT (Benzynowy, Automatyczna DCT);'
    assert expected_car_type == car_type_text
    assert expected_engine_type == engine_type_text