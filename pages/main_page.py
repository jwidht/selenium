from .base_page import BasePage
from .login_page import LoginPage
from .locators import BasePageLocators
from selenium.webdriver.common.by import By


class MainPage(BasePage):

    # def __init__(self, browser, url):
    #     super().__init__(browser, url)
    # class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)
        
    # def should_be_login_link(self):
    #     # self.browser.find_element(By.CSS_SELECTOR, "#login_link_invalid")
    #     assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not present"

    # def go_to_login_page(self):
    #     login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
    #     login_link.click() 
    #     #return LoginPage(browser=self.browser, url=self.browser.current_url) 


        

