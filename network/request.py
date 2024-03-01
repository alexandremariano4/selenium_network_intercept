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
        if url.endswith(route) and not is_filled:      
            try:
                if params.get('loaderId') and request.get('method') not in (None,'OPTIONS') :
                    object_intercepted.method = request['method']
                    is_filled = True
            except KeyError:...
            
            try:
                object_intercepted.method = params['headers'][':method']
                is_filled = True
            except KeyError:...
                
            try:
                object_intercepted.method = params['headers']['method']
                is_filled = True
            except KeyError:...
            
            if is_filled:
                return 'Método já preenchido'
            raise MethodError('method não encontrado')
        elif is_filled:
            return 'Método já preenchido'
        else:
            raise MethodError(f'Rota: {route} não foi encontrada na URL: {url} ')
    except (MethodError):
        method_error = True
        if method_error and not is_filled:
            object_intercepted.method = {
                'resposta' : 'method não encontrado, analisar dados abaixo',
                'erro': method_error,
                'url': url,
                'req': message
                }
