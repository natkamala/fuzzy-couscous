import pytest
from selenium import webdriver

@pytest.mark.ui
def test_track_parcel():
    driver = webdriver.Chrome()
    try:
        driver.get("https://novaposhta.ua/")
        search_field = driver.find_element_by_id('cargo_number')  # ID поля для введення номера відправлення
        search_field.send_keys('59001163580686')  # Приклад номера відправлення

        search_button = driver.find_element_by_id('cargo_number_submit')  # ID кнопки пошуку
        search_button.click()

        result_status = driver.find_element_by_class_name('expected-class-for-status')  # Клас елемента статусу
        assert "Доставлено" in result_status.text  # Приклад перевірки статусу

    finally:
        driver.close()
        