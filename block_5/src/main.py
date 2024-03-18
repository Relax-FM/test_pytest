from enum import Enum
from typing import Dict


class RequestType(Enum):
    GET = 'GET'
    POST = 'POST'
    PUT = 'PUT'
    DELETE = 'DELETE'


class ApiRequest:
    def __init__(self, payload: Dict, request_type: str):
        if not hasattr(RequestType, request_type):
            raise TypeError('Error: Please, select request type like POST GET PUT DELETE')
        self.request_type = RequestType(request_type)
        if request_type == RequestType.GET.value:
            if payload:
                raise AttributeError('Error: Please don\'t use payload when request type is GET')
            self.payload = None
        else:
            self.payload = payload

    def set_payload(self, new_payload: Dict):
        if self.request_type.value == RequestType.GET.value:
            if new_payload:
                raise AttributeError('Error: Please don\'t use payload when request type is GET')
            self.payload = None
        self.payload = new_payload
        return self.payload

    def get_payload(self):
        return self.payload

    def get_type(self):
        return self.request_type.value
