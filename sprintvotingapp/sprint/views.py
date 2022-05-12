import logging
from .models import Sprint
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import SprintSerializer
from rest_framework.exceptions import ValidationError
from .utils import InsertionError

logging.basicConfig(filename="sprint.log", filemode="w")


class SprintC(APIView):
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