from selenium import webdriver
from selenium.webdriver import ChromeOptions
from network_intercept import intercept_http
from pprint import pprint
import time

options = ChromeOptions()
options.add_argument('--log-level=3')
options.page_load_strategy = 'eager'
options.set_capability('goog:loggingPrefs', {'performance': 'ALL'})

initial_time = time.time()
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.delete_all_cookies()


driver.get('https://www.op.gg/statistics/champions')
end_time = time.time()


import time; time.sleep(10) #Manualmente vá e selecione algum das opções de busca (modo de jogo. nivel. regiao, periodo, position) para poder visualizar o retorno das queries, caso não seja selecionado, o interceptador retornará um objeto sem nenhum conteúdo já que não foi feito requisição de busca alguma.

response_body = intercept_http(
    driver,
    '/internal/bypass/statistics/'
    )

pprint(response_body.query_params)
pprint(response_body.url)

print(f"Tempo de execução do início da execução até a abertura do navegador: {end_time - initial_time:.2f} segundos")