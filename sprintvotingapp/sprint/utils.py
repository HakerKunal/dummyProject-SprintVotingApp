from rest_framework.response import Response
from django.http import QueryDict
from user.utils import EncodeDecodeToken


class InsertionError(Exception):
    """ my custom exception class """


class AlreadyPresentException(Exception):
    """ my custom exception class """


def verify_token(function):
    """
    For verifying user
    :param function:
    :return:
    """

    def wrapper(self, request, id=None):
        if 'HTTP_AUTHORIZATION' not in request.META:
            response = Response({'message': 'Token not provided in the header'})
            response.status_code = 400
            return response
        token = request.META['HTTP_AUTHORIZATION']
        user_id = EncodeDecodeToken.decode_token(token)

        if isinstance(request.data, QueryDict):
            request.data._mutable = True
        request.data.update({'user_id': user_id.get("user_id")})
        if id is None:
            return function(self, request)
        else:
            return function(self, request, id)

    return wrapper
