import json
from network.objected import ObjectIntercepted

has_error = False


def network_response(
    driver,
    params,
    message,
    route,
    url,
    object_intercepted : ObjectIntercepted,
    response,
    ):

    global has_error 
    

    
    try:
        # if 'route' in url:
        #     print('Debug') #Only to debug
        if route in url:
            try:                
                body = driver.execute_cdp_cmd('Network.getResponseBody', {'requestId': params['requestId']})
                try:
                    body_decoded = json.loads(body['body'])
                    object_intercepted.body = body_decoded
                except json.decoder.JSONDecodeError:
                    object_intercepted.body = body['body']        
            except (KeyError,Exception) as error: has_error = error


            try:
                object_intercepted.status_code = response['status']
            except KeyError as error: has_error = error
            
            try: 
                object_intercepted.url = response['url']
            except KeyError as error: has_error = error

            
    except:
        object_intercepted.error = {
            'erro': has_error,
            'resposta' : 'Parâmetro não encontrado',
            'url': url,
            }
