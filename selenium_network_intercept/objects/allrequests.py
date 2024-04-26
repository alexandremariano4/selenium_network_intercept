from typing import List
from dataclasses import dataclass, field
from selenium_network_intercept.objects.object_request import Request
from selenium_network_intercept.objects.object_response import Response

@dataclass
class AllRequests:

    __requests  :  list = field(default_factory=list)
    __responses :  list = field(default_factory=list)
    
    @property
    def requests(self) -> List[Request]:
        if self.__requests is None:
            return None
        return self.__requests.copy()
    
    @requests.setter
    def requests(self,requests):
        self.__requests.append(requests)

    @property
    def responses(self) -> List[Response]:
        if self.__responses is None:
            return None
        return self.__responses.copy()
    
    @responses.setter
    def responses(self,responses):
        self.__responses.append(responses)
        