from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium_network_intercept import intercept_http
import time

options = ChromeOptions()
options.add_argument('--log-level=3')
options.add_argument('--headless')
options.page_load_strategy = 'eager'
options.set_capability('goog:loggingPrefs', {'performance': 'ALL'})

initial_time = time.time()
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.delete_all_cookies()


url_completa = 'https://affiliates.video.globo.com/affiliates/info'

driver.get('https://www.globo.com/')
end_time = time.time()

requests = intercept_http(driver,only_request=True,static_resource=False)

for req in requests.requests:
    print(req.url)

print(f"Tempo de execução do início da execução até a abertura do navegador: {end_time - initial_time:.2f} segundos")