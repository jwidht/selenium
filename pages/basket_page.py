from .base_page import BasePage
# from .login_page import LoginPage
from .locators import BasketPageLocators
from selenium.webdriver.common.by import By


class BasketPage(BasePage):

    # def __init__(self, browser, url):
    #     super().__init__(browser, url)
    # class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(BasketPage, self).__init__(*args, **kwargs)

    def should_be_basket_url(self):
        # реализуйте проверку на корректный url адрес
        assert "basket" in self.browser.current_url, "No 'basket' in URL"

    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "Basket is not empty"

    def should_be_empty_basket_message(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET), "Empty message is not present"
        message = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET).text
        assert "Your basket is empty" in message
