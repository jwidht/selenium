from .base_page import BasePage
from .login_page import LoginPage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By


class ProductPage(BasePage):

    def __init__(self, browser, url):
        super().__init__(browser, url)

    def should_be_promo_url(self):
        # реализуйте проверку на корректный url адрес
        self.assert_in_url('promo')

    def should_be_add_to_basket_btn(self):
        # self.browser.find_element(By.CSS_SELECTOR, "#login_link_invalid")
        assert self.is_element_present(*ProductPageLocators.BTN_ADD_TO_BASKET), "BTN_ADD_TO_BASKET is not present"

    def should_be_h1(self):
        assert self.is_element_present(*ProductPageLocators.H1_TITLE), "H1_TITLE is not present"
        return self.browser.find_element(*ProductPageLocators.H1_TITLE).text
    
    def should_be_price(self):
        assert self.is_element_present(*ProductPageLocators.P_PRICE), "P_PRICE is not present"
        return self.browser.find_element(*ProductPageLocators.P_PRICE).text

    def should_be_alertinner(self,text):
        # self.browser.find_element(By.CSS_SELECTOR, "#login_link_invalid")
        assert self.is_element_present(*ProductPageLocators.ALERT_INNER), "ALERT_INNER is not present"
        actual_text = self.browser.find_element(*ProductPageLocators.ALERT_INNER).text
        assert text in actual_text
        assert text == actual_text , f"ALERT_INNER: expected {text}, actual {actual_text}"

    def should_be_alertinner_price(self,price_text):
        # self.browser.find_element(By.CSS_SELECTOR, "#login_link_invalid")
        assert self.is_element_present(*ProductPageLocators.P_PRICE), "P_PRICE is not present"
        actual_text = self.browser.find_element(*ProductPageLocators.P_PRICE).text
        assert price_text in actual_text
        assert price_text == actual_text , f"P_PRICE: expected {price_text}, actual {actual_text}"

    def click_btn_add_to_basket(self):
        btn_add_to_basket = self.browser.find_element(*ProductPageLocators.BTN_ADD_TO_BASKET)
        btn_add_to_basket.click() 

    def success_message_should_disappear(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE),"Success message is presented, but should not be"

    def success_message_should_disappear2(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE),"Success message is presented, but should not be"