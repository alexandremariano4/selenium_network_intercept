class Request:
    def __init__(
        self,
        tipo,
        network_method,
        url,
        status_code,
        headers
        ):
        self.type = tipo
        self.network_method = network_method
        self.url = url
        self.status_code = status_code
        self.headers = headers

