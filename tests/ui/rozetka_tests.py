import pytest
from selenium import webdriver

@pytest.mark.ui
def test_add_product_to_cart():
    driver = webdriver.Chrome()
    try:
        driver.get("https://rozetka.com.ua/")
        search_field = driver.find_element_by_css_selector('.search-form__input')  # Селектор поля пошуку
        search_field.send_keys('накопичуваач')

        search_button = driver.find_element_by_css_selector('.button_color_green')
        search_button.click()

        product_link = driver.find_element_by_css_selector('a.goods-tile__picture')  # Селектор першого товару у результатах
        product_link.click()

        add_to_cart_button = driver.find_element_by_css_selector('.buy-button__label')  # Селектор кнопки додавання в корзину
        add_to_cart_button.click()

        cart = driver.find_element_by_css_selector('.header-actions__button_type_basket')
        cart.click()

        # Перевірка, що товар доданий до корзини
        cart_item = driver.find_element_by_css_selector('.cart-product__main')  # Селектор товару в корзині
        assert 'накопичувач' in cart_item.text

    finally:
        driver.close()
        