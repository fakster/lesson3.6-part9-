from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_205/"
# link="https://selenium1py.pythonanywhere.com/ru/"


def test_contains_button_add_to_basket(browser):
    browser.get(link)
    button_add_to_basket = len(browser.find_elements_by_class_name('btn-add-to-basket'))
    assert button_add_to_basket > 0, "The page not contain  Button Add to Basket "
