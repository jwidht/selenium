from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):

    def __init__(self, browser, url):
        super().__init__(browser, url)

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url, "No 'login' in URL"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_LINK), "Login link is not present"
        assert self.is_element_present(*LoginPageLocators.PWD_LINK), "password is not present"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REG_EMAIL_LINK), "REG_EMAIL_LINK is not present"
        assert self.is_element_present(*LoginPageLocators.REG_PWD_LINK), "REG_PWD_LINK is not present"
        assert self.is_element_present(*LoginPageLocators.REG_PWD2_LINK), "REG_PWD2_LINK is not present"

    def register_new_user(self,email, password):
        self.browser.find_element(*LoginPageLocators.REG_EMAIL_LINK).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REG_PWD_LINK).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REG_PWD2_LINK).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REG_BUTTON).click()
        