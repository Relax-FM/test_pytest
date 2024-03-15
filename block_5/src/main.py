from enum import Enum


class RequestType(Enum):
    GET = 'GET'
    POST = 'POST'
    PUT = 'PUT'
    DELETE = 'DELETE'


class ApiRequest:
    def __init__(self, payload, request_type):
        self.payload = payload
        if not hasattr(RequestType, request_type):
            raise TypeError('Vse ploho deneg net')
        self.request_type = RequestType()

    def set_payload(self, new_payload):
        self.payload = new_payload

    def get_payload(self):
        return self.payload

    def get_type(self):
        return self.payload
