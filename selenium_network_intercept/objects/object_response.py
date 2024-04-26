class Response:
    def __init__(
        self,
        tipo,
        network_method,
        body,
        url,
        status_code,
        headers
        ):
        self.type = tipo
        self.body = body
        self.network_method = network_method
        self.url = url
        self.status_code = status_code
        self.headers = headers

