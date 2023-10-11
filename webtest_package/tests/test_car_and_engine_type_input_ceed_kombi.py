from . import (By, wait_to_be_visible, Select, time, driver,
               HomePage, configurationPage, converter_of_name, carConfigPage, ceed_kombi)

def test_configuration_button_test(driver):


    home_page = HomePage(driver)
    conf_page = configurationPage(driver)
    car_config_page = carConfigPage(driver)

    home_page.open()
    home_page.cookies_button_accept()
    home_page.configurator_button_click()
    conf_page.select_car_type_and_click('miejskie')
    conf_page.car_model_click('Ceed Kombi')
    time.sleep(3)
    car_config_page.choose_the_engine_click(ceed_kombi, 'BL', 1.5, 'Manualna')
    car_type_text = car_config_page.car_type_check_test('Business')
    engine_type_text = car_config_page.engine_type_check_test(1.5)
    expected_car_type = 'Business Line'
    expected_engine_type = '1.5 T-GDI 160KM 6MT (Benzynowy, Manualna);'
    assert expected_car_type == car_type_text
    assert expected_engine_type == engine_type_text
