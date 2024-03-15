from enum import Enum
from typing import Dict


class RequestType(Enum):
    GET = 'GET'
    POST = 'POST'
    PUT = 'PUT'
    DELETE = 'DELETE'


class ApiRequest:
    def __init__(self, payload: Dict, request_type: str):
        self.payload = payload
        if not hasattr(RequestType, request_type):
            raise TypeError('Vse ploho deneg net')
        self.request_type = RequestType(request_type)

    def set_payload(self, new_payload: Dict):
        self.payload = new_payload
        return self.payload

    def get_payload(self):
        return self.payload

    def get_type(self):
        return self.request_type.value
