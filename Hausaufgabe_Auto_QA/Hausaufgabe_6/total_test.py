import time

import pytest
from base_tests import BaseTest
from dotenv import load_dotenv
import os
load_dotenv()

class TestTotal(BaseTest):

    def test_product(self):

        self.login_page.success_login(os.getenv('USER_NAME'), os.getenv('PASSWORD'))
        product_element = self.product_page.all_items_are_displayed()
        assert product_element, "Login failed, inventory page not loaded"

        self.product_page.add_item_to_cart('Sauce Labs Backpack')
        self.product_page.add_item_to_cart('Sauce Labs Bolt T-Shirt')
        self.product_page.add_item_to_cart('Sauce Labs Onesie')
        self.product_page.go_to_cart()

        count_product_basket = self.basket_page.get_items_amount()
        assert count_product_basket == 3, f"Incorrect quantity of items in the cart: {count_product_basket}"
        self.basket_page.go_to_checkout()

        self.you_information_page.enter_firstname(os.getenv("FIRSTNAME"))
        self.you_information_page.enter_lastname(os.getenv("LASTNAME"))
        self.you_information_page.enter_zipcode(os.getenv("ZIPCODE"))

        self.you_information_page.go_to_overview()

        total_price = self.total_price_page.get_total_price()
        assert "$58.29" in total_price  , "Incorrect total amount"



