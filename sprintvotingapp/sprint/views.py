import logging
from .models import Sprint, Parameter
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import SprintSerializer, ParamSerializer
from rest_framework.exceptions import ValidationError
from .utils import InsertionError, verify_token

logging.basicConfig(filename="sprint.log", filemode="w")


class SprintC(APIView):
    @verify_token
    def post(self, request):
        """
        For Adding sprint Cycle
        :param request:
        :return:Response
        """
        try:
            serializer = SprintSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({"message": "Sprint Added Successfully",
                             "data": serializer.data},
                            status=status.HTTP_201_CREATED)
        except InsertionError as e:
            return Response({"message": "Error Occurred",
                             "error": str(e)},
                            status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"message": "Error Occurred",
                             "error": str(e)},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR
                            )

    @verify_token
    def put(self, request, id):
        """
        For Updating the Sprint Cycle
        :param request:
        :return:
        """
        try:
            sprint = Sprint.objects.get(id=id)
            serializer = SprintSerializer(sprint, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            return Response({
                "message": "Sprint updated successfully",
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        except ValidationError:
            logging.error("Validation failed")
            return Response(
                {
                    "message": "Sprint not updated"
                },
                status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({
                "message": "Error Occurred",
                "error": str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR, )

    @verify_token
    def get(self, request):
        """
             this method is created for retrieve data
             :param request: format of the request
             :return: Response
        """
        try:
            sprint = Sprint.objects.filter(is_active=True)
            serializer = SprintSerializer(sprint, many=True)
            if sprint:
                return Response({
                    "message": "Your active sprints are:",
                    "data": serializer.data
                })
            return Response({
                "message": "No active sprint",

            })

        except Exception as e:
            return Response({"message": str(e), })

    @verify_token
    def delete(self, request, id):
        """
        This method is created for delete the existing data
        :param request: format of the request
        :param id: sprint id
        :return: Response
        """
        try:
            sprint = Sprint.objects.get(id=id)
            sprint.delete()
            return Response(
                {
                    "message": "Sprint deleted successfully"
                },
                status=status.HTTP_200_OK)
        except ValidationError:
            logging.error("Validation failed")
            return Response(
                {
                    "message": "Sprint not deleted"
                },
                status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logging.error(e)
            return Response(
                {
                    "message": "no such sprint found",
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


class VoteParameter(APIView):
    @verify_token
    def post(self, request):
        """
        For Adding Parameter for voting
        :param request:
        :return: Response
        """
        try:
            serializer = ParamSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({
                "message": "Parameter Added Successful"
                           ""},
                status=status.HTTP_201_CREATED)
        except ValidationError:
            logging.error("Validation failed")
            return Response(
                {
                    "message": "validation failed"
                },
                status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:

            return Response({
                "message": "Error Occurred",
                "error": str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @verify_token
    def get(self, request):
        """
        For Getting the list of all the parameter
        :param request:
        :return:
        """
        try:
            parameters = Parameter.objects.all()
            serializer = ParamSerializer(parameters, many=True)
            return Response(
                {
                    "message": "Here your Parameters",
                    "data": serializer.data
                }, status=status.HTTP_200_OK
            )
        except ValidationError:
            logging.error("Validation failed")
            return Response(
                {
                    "message": "validation failed"
                },
                status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logging.error(e)
            return Response(
                {
                    "message": "Error Occurred",
                    "error": str(e),
                },
                status=status.HTTP_400_BAD_REQUEST)

    @verify_token
    def put(self, request, id):
        """
        USed for updating existing Parameter
        :param request:
        :param paramID: id of parameter you want to update
        :return:
        """
        try:
            parameter = Parameter.objects.get(id=id)
            serializer = ParamSerializer(parameter, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(
                {
                    "message": "Parameter updation  successful",
                    "data": serializer.data
                }
            )
        except ValidationError:
            return Response(
                {
                    "message": "Validation error"
                }
            )
        except Exception as e:
            logging.error(e)
            return Response(
                {
                    "message": "Error Occurred",
                    "error": str(e)
                }
            )
    @verify_token
    def delete(self,request, id):
        """
        For Delete The Existing Parameter
        :param id:id of the parameter you want to delete
        :return: Response
        """
        try:
            parameter = Parameter.objects.get(id=id)
            parameter.delete()
            return Response(
                {
                    "message": "Deletion Successful"
                }, status=status.HTTP_200_OK
            )
        except ValidationError:
            return Response(
                {
                    "message": "Validation error"
                }
            )
        except Exception as e:
            logging.error("Exception Occurred")
            return Response(
                {
                    "message": "Exception Occurred",
                    "error": str(e)
                }, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
