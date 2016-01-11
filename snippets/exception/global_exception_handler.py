from rest_framework.response import Response
from rest_framework.views import exception_handler

from snippets.exception.illegal_state_exception import IllegalStateException


def custom_exception_handler(exception, context):
    if isinstance(exception, IllegalStateException):
        return Response(exception.message, status=exception.status_code)

    return exception_handler(exception, context)
