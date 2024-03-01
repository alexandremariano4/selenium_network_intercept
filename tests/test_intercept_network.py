import json
from network.intercept import _fix_url,_get_url
from assertpy import assert_that
from network.response import network_response
from network.request import network_request
from network import (
    _mock_intercept_http_response,
    _mock_body,
    _mockChrome,
    _mock_intercept_http_response_error,
    _mock_params_get_url,
    _mock_intercept_http_request_method_in_request,
    _mock_intercept_http_request_method_in_headers,
    _mock_intercept_http_request_method_in_headers_without_two_points,
    _mock_intercept_http_request_method_error
    )
from network.objected import ObjectIntercepted


def test_get_url_response():
    _get_url(
        _mock_params_get_url.get('response')['url'],
        'response'
    )

def test_get_url_request():
    _get_url(
        _mock_params_get_url.get('request')['url'],
        'request'
    )

def test_fix_url_question_accent():
    assert_that(
    _fix_url('https://www.caminhosdamoda.sebraemg.com.br/conteudo?param="testes"&query="testador"')
    ).is_equal_to('https://www.caminhosdamoda.sebraemg.com.br/conteudo')

def test_fix_url_not_question_accent():
    assert_that(
    _fix_url('https://www.caminhosdamoda.sebraemg.com.br/conteudo')
    ).is_equal_to('https://www.caminhosdamoda.sebraemg.com.br/conteudo')

def test_intercept_http_response_success():
    objeto_teste = ObjectIntercepted('/conteudos')
    driver = _mockChrome
    network_response(
            driver=driver(False),
            params=_mock_intercept_http_response.get('params'),
            message=_mock_intercept_http_response,
            route='/conteudos',
            url='www.test.com.br/conteudos',
            object_intercepted=objeto_teste,
            response=_mock_intercept_http_response.get('params').get('response')
        )
    assert_that(objeto_teste.body).is_equal_to(
        json.loads(_mock_body.get('body').get('body'))
    )
    assert_that(objeto_teste.status_code).is_equal_to(200)
    assert_that(objeto_teste.url).is_equal_to(_mock_intercept_http_response.get('params').get('response').get('url'))

def test_intercept_http_response_body_error():
    objeto_teste = ObjectIntercepted('/conteudos')
    driver = _mockChrome
    network_response(
            driver=driver(True),
            params=_mock_intercept_http_response.get('params'),
            message=_mock_intercept_http_response,
            route='/conteudos',
            url='www.test.com.br/conteudos',
            object_intercepted=objeto_teste,
            response=_mock_intercept_http_response.get('params').get('response')
        )
    assert_that(objeto_teste.body).is_equal_to(
        {
            'erro': True,
            'resposta' : 'body não encontrado',
            'url': 'www.test.com.br/conteudos',
            'req': _mock_intercept_http_response
        }
    )

def test_intercept_http_response_status_code_error():
    objeto_teste = ObjectIntercepted('/conteudos')
    driver = _mockChrome
    network_response(
            driver=driver,
            params=_mock_intercept_http_response_error.get('params'),
            message=_mock_intercept_http_response_error,
            route='/conteudos',
            url='www.test.com.br/conteudos',
            object_intercepted=objeto_teste,
            response=_mock_intercept_http_response_error.get('params').get('response')
        )
    assert_that(objeto_teste.status_code).is_equal_to(
        {
            'erro': True,
            'resposta' : 'status code não encontrado',
            'url': 'www.test.com.br/conteudos',
            'req': _mock_intercept_http_response_error
        }
    )

def test_intercept_response_http_url_error():
    objeto_teste = ObjectIntercepted('/conteudos')
    driver = _mockChrome
    network_response(
            driver=driver,
            params=_mock_intercept_http_response.get('params'),
            message=_mock_intercept_http_response,
            route='/conteudos',
            url='www.test.com.br/conteudos',
            object_intercepted=objeto_teste,
            response=_mock_intercept_http_response_error.get('params').get('response')
        )
    assert_that(objeto_teste.url).is_equal_to(
        {
            'erro': True,
            'resposta' : 'url não encontrada',
            'url': 'www.test.com.br/conteudos',
            'req': _mock_intercept_http_response
        }
    )


def test_intercept_http_request_success_method_in_request():
    objeto_teste = ObjectIntercepted('/conteudos')
    network_request(
            params=_mock_intercept_http_request_method_in_request.get('params'),
            message=_mock_intercept_http_request_method_in_request,
            route='/conteudos',
            url='www.test.com.br/conteudos',
            object_intercepted=objeto_teste,
            request=_mock_intercept_http_request_method_in_request.get('params').get('request')
        )
    assert_that(objeto_teste.method).is_equal_to(
        _mock_intercept_http_request_method_in_request.get('params').get('request').get('method')
    )

def test_intercept_http_request_success_method_in_headers():
    objeto_teste = ObjectIntercepted('/conteudos')
    network_request(
            params=_mock_intercept_http_request_method_in_headers.get('params'),
            message=_mock_intercept_http_request_method_in_headers,
            route='/conteudos',
            url='www.test.com.br/conteudos',
            object_intercepted=objeto_teste,
            request=_mock_intercept_http_request_method_in_headers.get('params').get('request')
        )
    assert_that(objeto_teste.method).is_equal_to(
        _mock_intercept_http_request_method_in_headers.get('params').get('headers').get(':method')
    )

def test_intercept_http_request_success_method_in_headers_without_two_points():
    objeto_teste = ObjectIntercepted('/conteudos')
    network_request(
            params=_mock_intercept_http_request_method_in_headers_without_two_points.get('params'),
            message=_mock_intercept_http_request_method_in_headers_without_two_points,
            route='/conteudos',
            url='www.test.com.br/conteudos',
            object_intercepted=objeto_teste,
            request=_mock_intercept_http_request_method_in_headers_without_two_points.get('params').get('request')
        )
    assert_that(objeto_teste.method).is_equal_to(
        _mock_intercept_http_request_method_in_headers_without_two_points.get('params').get('headers').get('method')
    )

def test_intercept_http_request__method_error():
    objeto_teste = ObjectIntercepted('/conteudos')
    network_request(
            params=_mock_intercept_http_request_method_error.get('params'),
            message=_mock_intercept_http_request_method_error,
            route='/conteudos',
            url='www.test.com.br/conteudos',
            object_intercepted=objeto_teste,
            request=_mock_intercept_http_request_method_error.get('params').get('request')
        )
    assert_that(objeto_teste.method).is_equal_to(
        {
            'erro': True,
            'resposta' : 'method não encontrado, analisar dados abaixo',
            'url': 'www.test.com.br/conteudos',
            'req': _mock_intercept_http_request_method_error
        }
    )

def test_intercept_http_request__method_error_route():
    objeto_teste = ObjectIntercepted('/conteudos')
    network_request(
            params=_mock_intercept_http_request_method_error.get('params'),
            message=_mock_intercept_http_request_method_error,
            route='/conteudos',
            url='www.test.com.br/',
            object_intercepted=objeto_teste,
            request=_mock_intercept_http_request_method_error.get('params').get('request')
        )
    assert_that(objeto_teste.method).is_equal_to(
        {
            'erro': True,
            'resposta' : 'method não encontrado, analisar dados abaixo',
            'url': 'www.test.com.br/',
            'req': _mock_intercept_http_request_method_error
        }
    )

def test_intercept_http_request__method_error_many_params():
    objeto_teste = ObjectIntercepted('/conteudos')
    for i in range(0,3):
        retorno = network_request(
                params=_mock_intercept_http_request_method_in_request.get('params'),
                message=_mock_intercept_http_request_method_in_request,
                route='/conteudos',
                url='www.test.com.br/conteudos',
                object_intercepted=objeto_teste,
                request=_mock_intercept_http_request_method_in_request.get('params').get('request')
            )
    assert_that(objeto_teste.method).is_equal_to(
        _mock_intercept_http_request_method_in_request.get('params').get('request').get('method')
    )
    assert_that(retorno).is_equal_to('Método já preenchido')