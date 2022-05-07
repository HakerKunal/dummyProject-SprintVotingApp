import logging
from django.contrib import auth
from django.db import IntegrityError
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError
from .serializers import UserSerializer
from .utils import EncodeDecodeToken

logging.basicConfig(filename="user.log", filemode="w")


class Registration(APIView):
    def post(self, request):
        """
        Will be Used to Create or Add the User into User Table
        :return:Response
        """
        try:
            serializer = UserSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = serializer.create(validated_data=serializer.data)
            token = EncodeDecodeToken.encode_token(user.id)

            return Response({"message": "User Registration Successful"}, status=status.HTTP_201_CREATED)
        except IntegrityError as e:
            return Response(
                {
                    "message": "Same user already exist"
                },
                status=status.HTTP_400_BAD_REQUEST)

        except ValidationError:
            logging.error("Validation failed")
            return Response(
                {
                    "message": "validation failed"
                },
                status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logging.error("storing failed")
            return Response(
                {
                    "message": "User Registration Unsuccessful"
                },
                status=status.HTTP_400_BAD_REQUEST)


class Login(APIView):
    def post(self, request):
        try:
            username = request.data.get("username")
            password = request.data.get("password")
            user = auth.authenticate(username=username, password=password)
            if not user:
                return Response(
                    {
                        "message": "Login Unsuccessful username or password incorrect"
                    },
                    status=status.HTTP_404_NOT_FOUND)
            return Response(
                {
                    "message": "Login Successful"
                },
                status=status.HTTP_200_OK)

        except ValidationError as e:
            return Response(
                {
                    "message": "Authentication Fail",
                    "error": str(e)
                },
                status=status.HTTP_400_BAD_REQUEST)
