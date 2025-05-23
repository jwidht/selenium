import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en', #None, #'en',
                     help="Choose language en or ru")
                    
@pytest.fixture(scope="function")
def browser(request):
    print("\n ████████ start browser for test..██████")
    user_language = request.config.getoption("language")
    print(f"user_language={user_language}")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\n_______quit browser...______")
    browser.quit()
   
    
