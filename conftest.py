import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

"""
    добавляем парсер при запуске `pytest -s -v --browser_name=chrome test_parser.py` передать название браузера
    также можно прописать по дефолту открывать браузер без передачи параметра
    `pytest -v --tb=line --reruns 1 --browser_name=chrome --language=ru test_parser.py` // to choose language
"""

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default="en",
                     help="Choose language: ru,en....etc")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    browser = None
    if browser_name == "chrome":
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox(firefox_profile=fp)
    yield browser
    print("\nquit browser..")
    browser.quit()