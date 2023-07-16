from .base_page import BasePage
from .locators import BasketPageLocators
class BasketPage(BasePage):
    def should_not_be_items(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY), "Basket is not empty"
    def should_be_items(self):
        pass