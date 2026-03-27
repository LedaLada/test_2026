import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture()
def browser():
   options = Options()
   options.add_argument('--headless')
   browser = webdriver.Chrome(options=options)
   browser.implicitly_wait(10)
   browser.get('https://demoblaze.com/')
   yield browser