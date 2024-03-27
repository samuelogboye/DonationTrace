import logging
from uuid import uuid4

from django.http import JsonResponse

from core.exception_handlers import ErrorEnum, ErrorResponse

LOGGER = logging.getLogger(__name__)


class RequestIDMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.uid = uuid4()

        response = self.get_response(request)
        return response


class ExceptionHandlerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        return response

    def process_exception(self, request, exception):
        LOGGER.error(
            "An exception occurred: %s, Request_ID: %s",
            str(exception),
            request.uid,
            exc_info=True,
        )
        response = ErrorResponse(ErrorEnum.ERR_003, extra_detail=request.uid)
        return JsonResponse(data=response.data, status=response.status_code)
