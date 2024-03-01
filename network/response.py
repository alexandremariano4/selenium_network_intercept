import json
from network.objected import ObjectIntercepted

body_error = False
status_code_error = False
url_error = False
geral_error = False


def network_response(
    driver,
    params,
    message,
    route,
    url,
    object_intercepted : ObjectIntercepted,
    response,
    ):

    global body_error 
    global status_code_error 
    global url_error 
    global geral_error 
    

    
    try:
        # if 'route' in url:
        #     print('Debug') #Only to debug
        if route in url:
            try:                
                body = driver.execute_cdp_cmd('Network.getResponseBody', {'requestId': params.get('requestId')})
                try:
                    body_decoded = json.loads(body['body'])
                    object_intercepted.body = body_decoded
                except json.decoder.JSONDecodeError:
                    object_intercepted.body = body['body']        
            except:
                body_error = True
                if body_error: 
                    object_intercepted.body = {
                    'erro': body_error,
                    'resposta' : 'body não encontrado',
                    'url': url,
                    'req': message
                    }

            try:
                object_intercepted.status_code = response['status']
            except:
                status_code_error = True
                if status_code_error: 
                    object_intercepted.status_code = {
                    'erro': status_code_error,
                    'resposta' : 'status code não encontrado',
                    'url': url,
                    'req': message
                    }

            try: 
                object_intercepted.url = response['url']
            except:
                url_error = True
                if url_error: 
                    object_intercepted.url = {
                        'erro': url_error,
                        'resposta' : 'url não encontrada',
                        'url': url,
                        'req': message
                        }
    except:
        geral_error = True
        object_intercepted.error = {
            'erro': geral_error,
            'resposta' : 'Erro não mapeado, analisar dados abaixo',
            'url': url,
            'req': message
            }
