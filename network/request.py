import json
from network.objected import MethodError

method_error = False
is_filled = False

def network_request(
    params,
    message,
    route,
    url,
    object_intercepted,
    request
):
    
    global is_filled
    global method_error
    
    if object_intercepted.method is None:
        is_filled = False
    
    try:
        if route in url and not is_filled:      
            try:
                if params.get('loaderId') and request.get('method') not in (None,'OPTIONS') :
                    object_intercepted.method = request['method']
                    is_filled = True
            except KeyError as error: method_error = error
            
            try:
                object_intercepted.method = params['headers'][':method']
                is_filled = True
            except KeyError as error: method_error = error
                
            try:
                object_intercepted.method = params['headers']['method']
                is_filled = True
            except KeyError as error: method_error = error

            if is_filled:
                return 'Método já preenchido'
        
        elif is_filled:
            return 'Método já preenchido'
        else:
            raise MethodError(f'Rota: {route} não foi encontrada na última URL: {url}, verifique a lista de responses se está retornando a URL desejada.')
        
    except MethodError as error:
        method_error = error
        if method_error and not is_filled:
            object_intercepted.method = {
                'resposta' : 'Parâmetro method não encontrado',
                'erro': method_error,
                'url': url,
                }
