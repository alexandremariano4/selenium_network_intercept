from typing import List
from dataclasses import dataclass
from selenium_network_intercept.objects.allrequests import AllRequests
from selenium_network_intercept.objects.object_request import Request
from selenium_network_intercept.objects.object_response import Response

class AttributeEmpty(Exception):...
class MethodError(Exception):...
class UrlNotFoundError(Exception):...

@dataclass
class ObjectIntercepted(AllRequests):
    """
    Classe para representar uma solicitação HTTP interceptada.

    Args:
        route (str): O caminho da solicitação interceptada.
        list_of_responses (list): A lista de URLs das respostas interceptadas.
        list_of_requests (list): A lista de URLs das solicitações interceptadas.

    Attributes:
        _body (list): O corpo da solicitação interceptada.
        _status_code (int): O código de status da solicitação interceptada.
        _url (str): A URL da solicitação interceptada.
        _method (str): O método HTTP da solicitação interceptada.
        _error (str): O erro da solicitação interceptada.
        route (str): O caminho da solicitação interceptada.
        list_of_responses (list): A lista de URLs das respostas interceptadas.
        list_of_requests (list): A lista de URLs das solicitações interceptadas.
    """
    
    def __init__(self,part_of_route,driver):
        super().__init__()
        if part_of_route:
            self.part_of_route = part_of_route 
        self.part_of_route = None
        self.driver = driver
    
    
    def update(self):
        from selenium_network_intercept.intercept import intercept_http
        intercept_http(self.driver,only_request=True,update=True,update_object=self)
    
    __body : list = None 
    __status_code : int = None 
    __url : str = None 
    __method : str = None 
    __error : any = None
    __time : str = None 
    __query_params : dict = None 
    
    method_error = False
    is_filled = False
    has_error = False
    
    @property
    def body(self):
        if self.__body is None:
            return None
        return self.__body
    
    @body.setter
    def body(self,body):
        self.__body = body

    @property
    def status_code(self):
        if self.__status_code is None:
            return None
        return self.__status_code
    
    @status_code.setter
    def status_code(self, status_code):
        self.__status_code = status_code
        
    @property
    def url(self):
        if self.__url is None:
            return None
        return self.__url
    
    @url.setter
    def url(self, url):
        self.__url = url
        
    @property
    def method(self):
        if self.__method is None:
            return None
        return self.__method
    
    @method.setter
    def method(self, method):
        self.__method = method

    @property
    def error(self):
        if self.__error is None:
            return None
        return self.__error
    
    @error.setter
    def error(self,error):
        self.__error = error
    
    @property
    def time(self):
        if self.__time is None:
            return None
        return self.__time
    
    @time.setter
    def time(self,time):
        self.__time = f"{time:.2f}"
        
    @property
    def query_params(self):
        if self.__query_params is None:
            return None
        return self.__query_params
    
    @query_params.setter
    def query_params(self,query_params):
        self.__query_params = query_params

    def add_request(self,request):
        self.requests = request
    
    def add_response(self,response):
        self.responses = response

    def get_requests(self) -> List[Request]:
        return self.requests
    
    def get_responses(self) -> List[Response]:
        return  self.responses
