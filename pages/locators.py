from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.XPATH, "//span[@class='btn-group']/a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_PASS = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_PASS_CONFIRM = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_SUBMIT = (By.NAME,'registration_submit')
class ProductPageLocators():
    ADD_ITEM_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    ITEM_PRICE = (By.XPATH, "//p[@class='price_color']")
    ITEM_NAME = (By.CSS_SELECTOR, "h1")
    BASKET_NAME = (By.XPATH, "//div[@id='messages']/div[1]//strong")
    BASKET_PRICE = (By.XPATH, "//div[@id='messages']/div[3]//strong")

class BasketPageLocators():
    BASKET_EMPTY = (By.XPATH, "//*[text()[contains(., 'Your basket is empty')]]")