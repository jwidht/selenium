from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    # <a class="btn btn-default" href="/en-gb/basket/">View basket</a>
    BASKET_BUTTON = (By.CSS_SELECTOR, "span.btn-group > a.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    #LOGIN_LINK = (By.ID, "#registration_link")

class LoginPageLocators():
    LOGIN_LINK = (By.ID, "id_login-username")
    PWD_LINK = (By.ID, "id_login-password") 
    REG_EMAIL_LINK = (By.ID, "id_registration-email")
    REG_PWD_LINK = (By.ID, "id_registration-password1") 
    REG_PWD2_LINK = (By.ID, "id_registration-password2") 
    REG_BUTTON = (By.NAME, "registration_submit")

class ProductPageLocators():
    BTN_ADD_TO_BASKET = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    H1_TITLE = (By.CSS_SELECTOR, "h1")
    P_PRICE = (By.CSS_SELECTOR, "p.price_color")
    ALERT_INNER = (By.CSS_SELECTOR, "div.alertinner > strong")
    SUCCESS_MESSAGE= (By.CSS_SELECTOR, "div.alert-success")
    P_TOTAL = (By.CSS_SELECTOR, "div.alertinner > p > strong")
    # PWD_LINK = (By.ID, "id_login-password") 
    # REG_EMAIL_LINK = (By.ID, "id_registration-email")
    # REG_PWD_LINK = (By.ID, "id_registration-password1") 
    # REG_PWD2_LINK = (By.ID, "id_registration-password2") 

class BasketPageLocators():
    BTN_GO_TO_BASKET = (By.CSS_SELECTOR, "div.basket-mini.pull-right.hidden-xs > span > a")
    # <div id="content_inner"> <p> Your basket is empty.<a href="/en-gb/">Continue shopping</a> </p></div>
    EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner > p ")
    BASKET_ITEMS = (By.CSS_SELECTOR, "div.basket-items")
 