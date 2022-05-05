from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError


class Registration(APIView):
    def get(self):
        """
        Will be Used to Create or Add the User into User Table
        :return:Response
        """
        try:
            return Response({"message": "User Registration Successfull"})
        except ValidationError as e:
            return Response({"message": "User Registration Unsuccessful"})
