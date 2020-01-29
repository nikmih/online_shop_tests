import pytest
from selenium import webdriver
import time

def test_guest_should_see_add_to_basket_button(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(10)
    button = len(browser.find_elements_by_class_name("btn-add-to-basket"))
    assert button > 0 , "Element was not found"
    