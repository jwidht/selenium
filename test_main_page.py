from .pages.main_page import MainPage
from .pages.login_page import LoginPage
import time, pytest
from .pages.basket_page import BasketPage

# pytest -v -s --tb=line --language=en test_main_page.py

#link = #http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=midsummer"
link = "http://selenium1py.pythonanywhere.com/"

#def test_guest_can_go_to_login_page(browser):
#   #link = "http://selenium1py.pythonanywhere.com/"
#   page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
#   page.open()                      # открываем страницу
#   page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина


# def test_guest_should_see_login_link(browser):
#     #link = "http://selenium1py.pythonanywhere.com/"
#     page = MainPage(browser, link)
#     page.open()
#     page.should_be_login_link()
    
# def test_guest_can_go_to_login_page(browser):
#     #link = "http://selenium1py.pythonanywhere.com"
#     page = MainPage(browser, link)
#     page.open()
#     #login_page = page.go_to_login_page()
#     #login_page.should_be_login_page()
#     page.go_to_login_page()
#     login_page = LoginPage(browser, browser.current_url)
#     login_page.should_be_login_page()

# def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
#     page = MainPage(browser, link)
#     page.open()
#     # p2 = 
#     page.go_to_basket_page()
#     p2 = BasketPage(browser=browser, url=browser.current_url)
#     p2.should_be_empty_basket()
#     p2.should_be_empty_basket_message()

    # time.sleep(30 )

# pytest -v -s -m login_guest --tb=line --language=en test_main_page.py

@pytest.mark.login_guest
class TestLoginFromMainPage():

    # @pytest.fixture(scope="function", autouse=True)
    # def setup(self):
    #     self.product = ProductFactory(title = "Best book created by robot")
    #     # создаем по апи
    #     self.link = self.product.link # now can use self.link
    #     yield
    #     # после этого ключевого слова начинается teardown
    #     # выполнится после каждого теста в классе
    #     # удаляем те данные, которые мы создали 
    #     self.product.delete()
        
    def test_guest_can_go_to_login_page(self, browser):     
        #link = "http://selenium1py.pythonanywhere.com"
        page = MainPage(browser, link)
        page.open()
        #login_page = page.go_to_login_page()
        #login_page.should_be_login_page()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        #link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()
