from enum import Enum


class RequestType(Enum):
    GET = 'GET'
    POST = 'POST'
    PUT = 'PUT'
    DELETE = 'DELETE'


class ApiRequest:
    def __init__(self, payload, request_type: RequestType):
        self.payload = payload
        self.request_type = request_type

    def set_payload(self, new_payload):
        self.payload = new_payload
