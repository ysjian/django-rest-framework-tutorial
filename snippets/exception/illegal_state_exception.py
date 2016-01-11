from rest_framework.exceptions import APIException
from rest_framework.response import Response
from rest_framework.views import exception_handler


class IllegalStateException(Exception):
    default_status_code = 400

    def __init__(self, message, status_code=default_status_code):
        self.message = message
        self.status_code = status_code
