from selenium.webdriver import Chrome
import json

_mock_intercept_http_response =   {'params': {
        'response': {
            'status': 200,
            'url': 'www.test.com.br/conteudos'
        },
        'requestId': '1546.321',
    }
    }

_mock_intercept_http_response_error =   {'params': {
        'response': {
            'raise': 'error_status_code',
            'raise2': 'error_url'
        },
        'requestId': '1546.321',
    }
    }

_mock_intercept_http_request_method_in_request =   {'params': {
        'loaderId':'1239.456',
        'request': {
            'method': 'GET-REQUEST',
            'url': 'www.test.com.br/conteudos'
        },
        'requestId': '1546.321',
    }
}

_mock_intercept_http_request_method_in_headers =   {'params': {
        'headers': {
            ':method': 'GET-HEADERS',
        },
        'request': {
            'url': 'www.test.com.br/conteudos'
        },
        'requestId': '1546.321',
    }
}

_mock_intercept_http_request_method_in_headers_without_two_points =   {'params': {
        'headers': {
            'method': 'GET-HEADERS-WITHOUT-TWO-POINTS',
        },
        'request': {
            'url': 'www.test.com.br/conteudos'
        },
        'requestId': '1546.321',
    }
}

_mock_intercept_http_request_method_error =   {'params': {
        'loaderId':'1239.456',
        'request': {
            'raise': 'method-error',
            'url': 'www.test.com.br/conteudos'
        },
        'requestId': '1546.321',
    }
}

_mock_body = {
    'base64Encoded': False,
    'body': { 
        'id' : 1,
        'body': '{"teste":"texto de teste aleatório"}'
            }
    }

_mock_params_get_url = {
    'response': {
        'url': 'www.test.com.br/conteudos'
    },
    'request': {
        'url': 'www.test.com.br/conteudos'
    } 
}

class _mockChrome(Chrome):
    
    def __init__(self,error):
        self.error = error
        
    global _mock_body
    
    def execute_cdp_cmd(self,cmd: str, cmd_args: dict):
        if self.error == True:
            return None
        return _mock_body.get('body')
    
