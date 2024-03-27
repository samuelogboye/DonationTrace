from enum import Enum

from drf_spectacular.utils import extend_schema
from rest_framework import serializers, status
from rest_framework.fields import empty
from rest_framework.response import Response
from rest_framework.views import exception_handler


class ErrorEnum(Enum):
    ERR_001 = (
        "Validation Error",
        status.HTTP_400_BAD_REQUEST,
        "The request data failed validation. Please check your input and try again.",
    )
    ERR_002 = (
        "Authentication Error",
        status.HTTP_401_UNAUTHORIZED,
        "Authentication credentials were not provided.",
    )
    ERR_003 = (
        "Internal Server Error",
        status.HTTP_500_INTERNAL_SERVER_ERROR,
        "Something went wrong on our end. Please try again later.",
    )
    ERR_004 = (
        "Permission Error",
        status.HTTP_403_FORBIDDEN,
        (
            "Authentication credentials are either missing or the user lacks the"
            " necessary permissions to perform this action."
        ),
    )
    ERR_005 = (
        "Invalid Request Method",
        status.HTTP_405_METHOD_NOT_ALLOWED,
        "Accessing the resource with an unsupported method.",
    )
    ERR_006 = (
        "Not Found",
        status.HTTP_404_NOT_FOUND,
        "Resource does not exist",
    )


class ErrorResponse(Response):
    """
    Represents an error response to be returned from an API endpoint.

    Args:
        code (ErrorEnum): An enumeration representing the error code.
        serializer_errors (dict, optional): A dictionary of serializer validation errors.
            If provided, it would contain field names as keys and error information as values.
            Defaults to None.
        extra_detail (str, optional): Additional details or context for the error. Defaults to None.
        status (int, optional): The HTTP status code for the error response.
            If not provided, it defaults to the status associated with the provided error code.
        headers (dict, optional): Additional headers to include in the response. Defaults to None.

    Attributes:
        data (dict): A dictionary containing error information, including the error code,
            error message, and validation error details.
            If `serializer_errors` is provided, it includes validation error details for each field.
        status_code (int): The HTTP status code for the error response.

    Example:
        To create an error response with a specific error code and additional details:

        >>> error_response = ErrorResponse(
        ...     code=ErrorEnum.ERR_001,
        ...     extra_detail="Invalid input data",
        ...     headers={"X-Custom-Header": "Value"}
        ... )
    """

    def __init__(
        self,
        code: ErrorEnum,
        serializer_errors: dict = None,
        extra_detail: str = None,
        status: int = None,
        headers: dict = None,
    ):
        super().__init__(None, status=status or code.value[1])

        error_data = {
            "error_code": code.name,
            "error": code.value[0],
            "detail": (
                [
                    {"loc": ["body", field], "msg": error[0], "type": error[0].code}
                    for field, error in serializer_errors.items()
                ]
                if serializer_errors
                else code.value[2]
            ),
        }

        if extra_detail:
            error_data["extra_detail"] = extra_detail

        self.data = error_data

        if headers:
            for name, value in headers.items():
                self[name] = value


def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    if response is not None:
        if isinstance(response.data, list):
            # The case of serializer.ValidationError been raised.
            response.data = {"non-field": response.data}

        if password_errors := check_password(response.data):
            # Remove any other password errors aside from the one processed and returned
            response.data = {
                k: v for k, v in response.data.items() if "password" not in v[0].code
            }
            response.data = response.data | password_errors

        if response:
            result = [
                code for code in ErrorEnum if code.value[1] == response.status_code
            ]

            custom_response = ErrorResponse(
                code=result[0],
                status=response.status_code,
                serializer_errors=(
                    response.data
                    if response.status_code == status.HTTP_400_BAD_REQUEST
                    else None
                ),
            )
            return custom_response
    return response


def check_password(exc: dict):
    if error_list := exc.get("non_field_errors", None):
        if any("password" in error.code for error in error_list):
            error_dict = {
                f"password{index}": [error] for index, error in enumerate(error_list, 1)
            }

            return error_dict

    return None


class ErrorSerializer(serializers.Serializer):
    class MyEnumField(serializers.ChoiceField):
        def __init__(self, *args, **kwargs):
            choices = [(e.name, e.value[0]) for e in ErrorEnum]
            super().__init__(choices=choices, *args, **kwargs)

    error_code = MyEnumField()
    error = serializers.CharField()
    detail = serializers.CharField()
    extra_detail = serializers.CharField()


class ValidationErrorSerializer(ErrorSerializer):
    detail = serializers.ListField(child=serializers.CharField())


def response_schemas(
    response_model: serializers.Serializer = None,
    code: int = 200,
    schema_response_codes: list = [],
):
    """
    Example usage:
    ```For default 200_OK response
        @response_schemas(response_model=MyModelSerializer)
        class my_view(request):
            # Your view logic here
            ...

       For default 201_CREATED response
        @response_schemas(response_model=MyModelSerializer, code = 201, schema_response_codes=[400, 401])
        class my_view(request):
            # Your view logic here
            ...

       For default 200_OK response and extra codes
        @response_schemas(response_model=MyModelSerializer, schema_response_codes=[400, 401])
        class my_view(request):
            # Your view logic here
            ...
    ```
    """
    if response_model and 200 in schema_response_codes:
        raise AssertionError(
            "response_model and 200 in schema_response_codes are mutually exclusive,"
            " choose one"
        )

    error_dict = {code: response_model}
    for code in schema_response_codes:
        if isinstance(code, int):
            if code == status.HTTP_400_BAD_REQUEST:
                error_dict[code] = ValidationErrorSerializer
            else:
                error_dict[code] = ErrorSerializer
    return extend_schema(responses=error_dict if error_dict else empty)
