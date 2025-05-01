from .pages.main_page import MainPage
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
import pytest
import time
from .pages.basket_page import BasketPage

# pytest -v -s --tb=line --language=en test_product_page.py
# pytest -v --tb=line --language=en -m need_review

link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

# @pytest.mark.parametrize('linknumber', [  "0"
#                                         # ,
#                                         #    "1", "2", "3", "4", "5", "6",
#                                         #      pytest.param("7", marks=pytest.mark.xfail), # "7", 
#                                         #      "8", "9"
#    
@pytest.mark.need_review                                     ])
def test_guest_can_add_product_to_basket(browser, linknumber):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{linknumber}"
    print(link)
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_basket_btn()
    page.should_be_h1()
    title = page.should_be_h1()
    price = page.should_be_price()
    page.click_btn_add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_alertinner(title)
    page.should_be_alertinner_price(price)
    time.sleep(4)
    page.success_message_should_disappear() #элемент присутствует на странице и должен исчезнуть
    print("-OK-")
    time.sleep(30)
'''
<div class="alertinner "><strong>Coders at Work</strong> has been added to your basket.</div>

<div class="alertinner ">
<p>Your basket total is now <strong>£19.99</strong>
</p>

<div class="alert alert-safe alert-noicon alert-success  fade in">
        <a class="close" data-dismiss="alert" href="#">×</a>
        <div class="alertinner ">
<strong>Coders at Work</strong> has been added to your basket.
        </div>
    </div>
'''

# def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
#     page = ProductPage(browser, link)
#     page.open()
#     page.click_btn_add_to_basket()
#     page.solve_quiz_and_get_code()
#     page.success_message_should_disappear()
#     print("TEST FINISHED")

# def test_guest_cant_see_success_message(browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
#     page = ProductPage(browser, link)
#     page.open()
#     page.success_message_should_disappear()
#     print("TEST FINISHED") 

# def test_message_disappeared_after_adding_product_to_basket(browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
#     page = ProductPage(browser, link)
#     page.open()
#     page.click_btn_add_to_basket()
#     page.solve_quiz_and_get_code()
#     page.success_message_should_disappear2()
#     print("TEST FINISHED")

# def test_guest_should_see_login_link_on_product_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
#     page = ProductPage(browser, link)
#     page.open()
#     page.should_be_login_link()
@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    # p2 = 
    page.go_to_basket_page()
    p2 = BasketPage(browser=browser, url=browser.current_url)
    p2.should_be_empty_basket()
    p2.should_be_empty_basket_message()
 
class TestUserAddToBasketFromProductPage:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time())
        link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        page = LoginPage(browser, link)
        page.open()
        page.register_new_user(email, password)
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self,browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
        page = ProductPage(browser, link)
        page.open()
        page.success_message_should_disappear()
        print("TEST FINISHED") 
    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self,browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
        print(link)
        page = ProductPage(browser, link)
        page.open()
        page.should_be_add_to_basket_btn()
        page.should_be_h1()
        title = page.should_be_h1()
        price = page.should_be_price()
        page.click_btn_add_to_basket()
        page.solve_quiz_and_get_code()
        page.should_be_alertinner(title)
        page.should_be_alertinner_price(price)
        time.sleep(4)
        page.success_message_should_disappear() #элемент присутствует на странице и должен исчезнуть
        print("-OK-")