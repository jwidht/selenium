# pytest -v --tb=line --language=en
# --tb=line- выводить только одну строку из лога каждого упавшего теста. 

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    browser.get(link)
    login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
    login_link.click()
