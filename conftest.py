import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='chrome',
                     help='Choose browser: chrome or firefox(waiting for the bug fix)')
    parser.addoption('--language', action='store', default="ru",    # default=None
                     help="Choose language: '--language=en' or '--language=ru'")


# pytest -s -v --browser=chrome --language=ru test_items.py
@pytest.fixture(scope='function')
def driver(request):
    
    browser = request.config.getoption('browser')
    user_language = request.config.getoption("language")
    
    match browser:
        case 'chrome':
            print('\nstart chrome browser for test..')
            options = Options()
            options.add_experimental_option('prefs', {'intl.accept_languages': user_language})

            driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
            driver.maximize_window()
        # case 'firefox':   # waiting for the bug fix driver firefox 28.12.2022
        #     driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        case _:
            raise pytest.UsageError('--browser should be chrome or firefox(waiting for the bug fix)')
            
    yield driver
    print('\nquit browser..')
    driver.quit()

