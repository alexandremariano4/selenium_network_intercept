from selenium import webdriver
from selenium.webdriver import ChromeOptions
from network.intercept import intercept_http
from pprint import pprint

options = ChromeOptions()
options.add_argument('--log-level=3')
options.add_argument('--headless')
options.set_capability('goog:loggingPrefs', {'performance': 'ALL'})

driver = webdriver.Chrome(options=options)
driver.delete_all_cookies()
driver.get('https://www.globo.com/')


response_body = intercept_http(
    driver,
    '/affiliates/info',
    delay=2)
pprint(response_body)

