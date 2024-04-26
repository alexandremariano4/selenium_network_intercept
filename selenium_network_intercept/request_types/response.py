import json
from selenium_network_intercept.objects.objected import ObjectIntercepted
from selenium_network_intercept.objects.object_response import Response


def network_response(
    driver,
    params,
    message,
    part_of_route,
    url,
    object_intercepted : ObjectIntercepted,
    response,
    *,
    only_requests
    ): 

    if not only_requests:
        try:
            if part_of_route in url:
                try:                
                    body = driver.execute_cdp_cmd('Network.getResponseBody', {'requestId': params['requestId']})
                    try:
                        if body['body'] == '':
                            object_intercepted.body = 'Sem conteúdo no body da requisição'
                        else:
                            body_decoded = json.loads(body['body'])
                            object_intercepted.body = body_decoded
                    except json.decoder.JSONDecodeError:
                        object_intercepted.body = body['body']        
                except (KeyError,Exception) as error: object_intercepted.has_error = error


                try:
                    object_intercepted.status_code = response['status']
                except KeyError as error: object_intercepted.has_error = error
                
                try: 
                    object_intercepted.url = response['url']
                except KeyError as error: object_intercepted.has_error = error

                
        except:
            object_intercepted.error = {
                'erro': object_intercepted.has_error,
                'resposta' : 'Parâmetro não encontrado',
                'url': url,
                }
    else:
        try:                
            body = driver.execute_cdp_cmd('Network.getResponseBody', {'requestId': params['requestId']})
            try:
                if body['body'] == '':
                    body = 'Sem conteúdo no body da requisição'
                else:
                    body_decoded = json.loads(body['body'])
                    body = body_decoded
            except json.decoder.JSONDecodeError:
                body = body['body']     
        except:
            body = 'Sem conteúdo no body da requisição'
        
        object_intercepted.responses = Response(
            tipo = 'Response',
            body = body,
            network_method = message['method'],
            url = url,
            status_code = params['response']['status'],
            headers = params['response']['headers']
        )
