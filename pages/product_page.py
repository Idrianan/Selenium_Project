from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_item_to_basket(self):
        btn = self.browser.find_element(*ProductPageLocators.ADD_ITEM_TO_BASKET)
        btn.click()
    
    def find_product_name(self):
        return self.browser.find_element(*ProductPageLocators.ITEM_NAME).text
    
    def find_product_price(self):
        return self.browser.find_element(*ProductPageLocators.ITEM_PRICE).text 
    
    def find_basket_name(self):
        return self.browser.find_element(*ProductPageLocators.BASKET_NAME).text 

    def find_basket_price(self):
        return self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text 

    def item_is_in_basket(self):
        assert self.find_product_name()==self.find_basket_name(), f'Invalid product name in busket. \nShould be {self.find_product_name()} but got {self.find_basket_name()}'
        assert self.find_product_price()==self.find_basket_price() , f'Invalid product price in busket. \nShould be {self.find_product_price()} but got {self.find_basket_price()}'