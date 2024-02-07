from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse

class TagCreatorView:
    def validata_and_create(self, http_request) -> HttpResponse:
        body = http_request.body
        product_code = body['product_code']
         