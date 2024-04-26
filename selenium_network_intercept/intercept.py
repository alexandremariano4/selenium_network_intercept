import time
import json
from selenium_network_intercept.exceptions.exceptions import CapabilityNotFound,ConflictingArgumentError,ArgumentNotRequestedError
from selenium_network_intercept.request_types.response import network_response
from selenium_network_intercept.request_types.request import network_request
from time import sleep
from selenium_network_intercept.objects.objected import ObjectIntercepted


def is_valid_url(url, static_resource : bool):
    is_valid = False
    extension = (
        '.html','.css','.jpg','.jpeg','.png','.woff','.woff2','.js','.ico','.gif','.svg','.php','.webp','.json','.dhtml',
        '.ghtml','js','css2','.bin')
    if not static_resource:
        try:
            if not(url.endswith(extension)):
                is_valid = True
        except:...
        try:
            if not(url.endswith(extension)):
                is_valid = True
        except:...
    if static_resource:
        is_valid = True
    return is_valid


def  _get_url(params,req_or_res):
    try:
        if req_or_res == 'response':
            url = _fix_url(params.get('response').get('url'))
        else:
            url = _fix_url(params.get('request').get('url'))
        return url
    except:...
    
    
def _fix_url(url):
    """_summary_

    Args:
        url (string): URL Completa da requisição

    Returns:
        string: treated_url = URL sem parametros de busca e querys.
        string: url = URL completa da requisição.
        
        
    """
    try:
        treated_url = url.split('?')[0]
        return treated_url
    except:
        return url


def verify_capabilities(driver):
    """
    Verifica se o driver contém a capacidade "performance" para interceptar requisições.
    """
    if 'performance' in driver.log_types:
        return None
    raise CapabilityNotFound(
        """O driver não contém a capacidade "performance" para interceptar requisições.
Verifique a documentação ou tente adicionar em sua instância do webdriver:

from selenium.webdriver import ChromeOptions
options = ChromeOptions()
options.set_capability('goog:loggingPrefs', {'performance': 'ALL'})
driver = webdriver.Chrome(options=options)"""
    )

def intercept_http(
    driver,
    part_of_route=None,
    *,
    only_request=False,
    static_resource=False,
    delay=5,
    update=False,
    update_object=None
    ) -> ObjectIntercepted:
    """
    Obs:
    Recomendado não utilizar a busca pela rota no início da execução do driver, visto que para ser interceptado, é necessário que as rotas já tenham sido finalizadas.
    Intercepta solicitações HTTP feitas por um WebDriver Selenium.
    Pode ser colocado qualquer parte da URL / Rota desejada, contando que não seja parte de uma query.

    Args:
        driver: Uma instância de WebDriver Selenium.
        part_of_route (str): Uma parte da URL para ser possível identificar a URL desejada
        only_request (default=False) : Envie True para retornar somente requisições, sem buscar especificamente por uma
        static_resource (default=False): Mudar para True caso queira que retorne arquivos estáticos
        delay: Tempo de espera para a captura dos logs
        update: Uso interno do sistema, não envie este parâmetro
        update_object: Uso interno do sistema, não envie este parâmetro
        

    Nota:
        Esta função intercepta solicitações HTTP feitas pela instância fornecida de WebDriver. Ela busca
        solicitações cujas URLs terminam com o sufixo especificado (`part_of_route`). Não sendo necessário enviar 
        informações como query na URL, somente a rota necessária.
        Para cada solicitação interceptada, ela recupera informações relevantes, como o corpo da solicitação, 
        código de status, URL e método HTTP, e as encapsula em uma instância de ObjectIntercepted.
        
        Caso envie static_resource False para não considerar arquivos estáticos, saiba que os arquivos serão os seguintes : ('.html','.css','.jpg','.jpeg','.png','.woff','.woff2','.js','.ico','.gif','.svg','.php','.webp','.json','.dhtml','.ghtml','js','css2','.bin') 
    """
    if part_of_route and only_request:
        raise ConflictingArgumentError('Não utilize os argumentos `part_of_route` e `only_request` juntos.')
    
    verify_capabilities(driver)
    
    initial_time = time.time()
    logs1 = driver.get_log('performance') 

    sleep(delay)
    if not update:
        object_intercepted = ObjectIntercepted(part_of_route,driver)
    else:
        object_intercepted = update_object
    logs2 = driver.get_log('performance')
    logs = logs1 + logs2
    
    
    for log in logs:
        message = json.loads(log.get('message')).get('message')
        params  = json.loads(log.get('message')).get('message').get('params')
        method  = json.loads(log.get('message')).get('message').get('method')
        response  = json.loads(log.get('message')).get('message').get('params').get('response')
        request  = json.loads(log.get('message')).get('message').get('params').get('request')

        response_url = _get_url(params,'response')
        request_url  = _get_url(params,'request')
        


        if 'Network.responseReceived' == method and is_valid_url(response_url,static_resource):
            network_response(
                driver,
                params,
                message,
                part_of_route,
                response_url,
                object_intercepted,
                response,
                only_requests=only_request
            )
        
        
        if 'Network.requestWillBeSent' == method and is_valid_url(request_url,static_resource):
            network_request(
                params,
                message,
                part_of_route,
                request_url,
                object_intercepted,
                request,
                only_request=only_request
            )
        
    end_time = time.time()
    object_intercepted.time = end_time - initial_time
    
    return object_intercepted
