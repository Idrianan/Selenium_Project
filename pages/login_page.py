from .base_page import BasePage
from .locators import LoginPageLocators
import time

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Url should contain login"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self,email,password):
        email_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
        pass_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASS)
        pass_field_confirm = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASS_CONFIRM)
        submit = self.browser.find_element(*LoginPageLocators.REGISTRATION_SUBMIT)
        email_field.send_keys(email)
        pass_field.send_keys(password)
        pass_field_confirm.send_keys(password)
        submit.click()