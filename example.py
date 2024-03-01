from selenium import webdriver
from selenium.webdriver import ChromeOptions
from network.intercept import intercept_http
from pprint import pprint
import time

options = ChromeOptions()
options.add_argument('--log-level=3')
options.headless = False
options.page_load_strategy = 'eager'
options.set_capability('goog:loggingPrefs', {'performance': 'ALL'})

initial_time = time.time()
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.delete_all_cookies()


url_completa = 'https://affiliates.video.globo.com/affiliates/info'

driver.get('https://www.globo.com/')
end_time = time.time()




response_body = intercept_http(
    driver,
    '/affiliates/info',
    delay=2)
pprint(response_body)
pprint(url_completa in response_body.get_list_of_responses())
pprint(url_completa in response_body.get_list_of_requests())
print(f"Tempo de execução do início da execução até a abertura do navegador: {end_time - initial_time:.2f} segundos")