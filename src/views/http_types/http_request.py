from typing import Dict

class HttpRequest:
    def __init__(
            self,
            header: Dict = None,
            body: Dict = None,
            quarry_params: Dict = None,
        ) -> None:
        self.header = header
        self.body = body
        self.quarry_params = quarry_params
        