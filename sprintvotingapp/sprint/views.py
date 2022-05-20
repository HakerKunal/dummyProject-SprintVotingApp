import logging
from collections import Counter
from itertools import count
from django.db import transaction
from .models import Sprint, Parameter, Votes
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import SprintSerializer, ParamSerializer, VoteSerializer
from rest_framework.exceptions import ValidationError
from .utils import InsertionError, AlreadyPresentException, verify_token
from user.models import User

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
            user = User.objects.get(id=request.data.get("user_id"))

            if user.is_superuser:
                serializer = SprintSerializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                return Response(
                    {
                        "message": "Sprint Added Successfully",
                        "data": serializer.data
                    }, status=status.HTTP_201_CREATED
                )
            return Response(
                {
                    "message": "Only admin or superuser can add a sprint"

                }, status=status.HTTP_401_UNAUTHORIZED
            )
        except InsertionError as e:
            return Response(
                {
                    "message": "Error Occurred",
                    "error": str(e)
                }, status=status.HTTP_400_BAD_REQUEST
            )
        except Exception as e:
            return Response(
                {"message": "Error Occurred",
                 "error": str(e)
                 }, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    @verify_token
    def put(self, request, id):
        """
        For Updating the Sprint Cycle
        :param request:
        :return:
        """
        try:
            user = User.objects.get(id=request.data.get("user_id"))
            if user.is_superuser:
                sprint = Sprint.objects.get(id=id)
                serializer = SprintSerializer(sprint, data=request.data)
                serializer.is_valid(raise_exception=True)
                serializer.save()

                return Response(
                    {
                        "message": "Sprint updated successfully",
                        "data": serializer.data
                    }, status=status.HTTP_200_OK
                )
            return Response(
                {
                    "message": "Only admin or superuser can update a sprint"

                }, status=status.HTTP_401_UNAUTHORIZED
            )
        except ValidationError:
            logging.error("Validation failed")
            return Response(
                {
                    "message": "Sprint not updated"
                },
                status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response(
                {
                    "message": "Error Occurred",
                    "error": str(e)
                }, status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

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
                return Response(
                    {
                        "message": "Your active sprints are:",
                        "data": serializer.data
                    }, status=status.HTTP_200_OK
                )
            return Response(
                {
                    "message": "No active sprint",
                }, status=status.HTTP_404_NOT_FOUND
            )

        except Exception as e:
            return Response(
                {
                    "message": "Error Occurred",
                    "error": str(e)
                }, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    @verify_token
    def delete(self, request, id):
        """
        This method is created for delete the existing data
        :param request: format of the request
        :param id: sprint id
        :return: Response
        """
        try:
            user = User.objects.get(id=request.data.get("user_id"))
            if user.is_superuser:
                sprint = Sprint.objects.get(id=id)
                sprint.delete()
                return Response(
                    {
                        "message": "Sprint deleted successfully"
                    },
                    status=status.HTTP_200_OK)
            return Response(
                {
                    "message": "Only admin or superuser can delete a sprint"

                }, status=status.HTTP_401_UNAUTHORIZED
            )
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
            user = User.objects.get(id=request.data.get("user_id"))
            if user.is_superuser:
                serializer = ParamSerializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                return Response({
                    "message": "Parameter Added Successful",
                    "data": serializer.data
                },
                    status=status.HTTP_201_CREATED)
            return Response(
                {
                    "message": "Only admin or superuser can add  parameter"

                }, status=status.HTTP_401_UNAUTHORIZED
            )
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
            user = User.objects.get(id=request.data.get("user_id"))
            if user.is_superuser:
                parameter = Parameter.objects.get(id=id)
                serializer = ParamSerializer(parameter, data=request.data)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                return Response(
                    {
                        "message": "Parameter updation  successful",
                        "data": serializer.data
                    }, status=status.HTTP_200_OK
                )
            return Response(
                {
                    "message": "Only admin or superuser can update parameter"

                }, status=status.HTTP_401_UNAUTHORIZED
            )
        except ValidationError:
            return Response(
                {
                    "message": "Validation error"
                }, status=status.HTTP_400_BAD_REQUEST
            )
        except Exception as e:
            logging.error(e)
            return Response(
                {
                    "message": "Error Occurred",
                    "error": str(e)
                }, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    @verify_token
    def delete(self, request, id):
        """
        For Delete The Existing Parameter
        :param id:id of the parameter you want to delete
        :return: Response
        """
        try:
            user = User.objects.get(id=request.data.get("user_id"))
            if user.is_superuser:
                parameter = Parameter.objects.get(id=id)
                parameter.delete()
                return Response(
                    {
                        "message": "Deletion Successful"
                    }, status=status.HTTP_200_OK
                )
            return Response(
                {
                    "message": "Only admin or superuser can delete parameter"

                }, status=status.HTTP_401_UNAUTHORIZED
            )
        except ValidationError:
            return Response(
                {
                    "message": "Validation error"
                }, status=status.HTTP_400_BAD_REQUEST
            )
        except Exception as e:
            logging.error("Exception Occurred")
            return Response(
                {
                    "message": "Exception Occurred",
                    "error": str(e)
                }, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class Voting(APIView):
    @transaction.atomic
    @verify_token
    def post(self, request, id):
        try:
            parameter_list = request.data.get("parameter_list")
            if not Sprint.objects.filter(id=id, is_active=True):
                return Response(
                    {
                        "message": "this Sprint is not active"
                    }, status=status.HTTP_400_BAD_REQUEST
                )
            with transaction.atomic():
                for parameter in parameter_list:
                    parameter.update({"sprint_id": id})
                    parameter.update({"vote_by": request.data.get("user_id")})

                    vote = Votes.objects.filter(vote_by=request.data.get("user_id"),
                                                parameter_id=parameter.get("parameter_id"),
                                                sprint_id=id)

                    if parameter.get("vote_by") == parameter.get("vote_to"):
                        raise InsertionError


                    elif vote:
                        raise AlreadyPresentException

                    serializer = VoteSerializer(data=parameter)
                    serializer.is_valid(raise_exception=True)
                    serializer.save()

            return Response(
                {
                    "message": "Voting Successful"
                }, status=status.HTTP_201_CREATED
            )
        except InsertionError:
            return Response(
                {
                    "message": "You cannot Vote for yourself",
                    "data": parameter
                }, status=status.HTTP_400_BAD_REQUEST
            )

        except AlreadyPresentException:
            return Response(
                {
                    "message": "Parameter addition Unsuccessful-already voted on this parameter",
                    "data": parameter
                }, status=status.HTTP_400_BAD_REQUEST
            )
        except Exception as e:
            logging.error(e)

            return Response(
                {
                    "message": "Exception Occurred",
                    "error": str(e)
                }, status=status.HTTP_400_BAD_REQUEST
            )

    @verify_token
    def get(self, request, id):
        """
        For getting the details of vote done by a user
        :param request:
        :param id: User id of how is login
        :return: Response
        """
        try:

            votes = Votes.objects.filter(vote_by=request.data.get("user_id"), sprint_id=id)
            serializer = VoteSerializer(votes, many=True)
            vote_list = list()
            if serializer.data:
                for vote in serializer.data:
                    vote_list.append({"parameter_id": vote.get("parameter_id"), "vote_to": vote.get("vote_to")})
                vote_data = {
                    "Vote_by": request.data.get("user_id"),
                    "sprint_id": id,
                    "vote_details": vote_list
                }
                return Response(
                    {
                        "message": "Here is your data",
                        "data": vote_data
                    }, status=status.HTTP_200_OK
                )
            return Response(
                {
                    "message": "He has Not vote for any parameter",

                }, status=status.HTTP_404_NOT_FOUND
            )
        except ValidationError:
            return Response(
                {
                    "message": "validation error"
                }, status=status.HTTP_400_BAD_REQUEST
            )
        except Exception as e:
            logging.error(e)
            return Response(
                {
                    "message": "Error Occurred",
                    "error": str(e)
                }, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    @verify_token
    def put(self, request, id):
        """
        For updating the existing votes
        :param request:
        :param id: Id of the sprint
        :return: Response
        """
        try:

            parameter_list = request.data.get("parameter_list")
            if not Sprint.objects.filter(id=id, is_active=True):
                return Response(
                    {
                        "message": "this Sprint is not active"
                    }, status=status.HTTP_400_BAD_REQUEST
                )
            for parameter in parameter_list:
                parameter.update({"sprint_id": id})
                parameter.update({"vote_by": request.data.get("user_id")})
                votes_obj = Votes.objects.filter(
                    vote_by=parameter.get("vote_by"),
                    parameter_id=parameter.get("parameter_id"),
                    sprint_id=parameter.get("sprint_id")
                ).first()
                if parameter.get("vote_by") == parameter.get("vote_to"):
                    return Response(
                        {
                            "Message": "You Can not update your self parameter",
                        },
                        status=status.HTTP_400_BAD_REQUEST
                    )
                else:
                    if votes_obj is None:
                        serializer = VoteSerializer(instance=votes_obj, data=parameter)
                        serializer.is_valid(raise_exception=True)
                        serializer.save()
                    else:
                        votes_obj.delete()
                        serializer = VoteSerializer(data=parameter)
                        serializer.is_valid(raise_exception=True)
                        serializer.save()
            return Response(
                {
                    "message": "Your vote is updated",

                }, status=status.HTTP_200_OK
            )
        except ValidationError as e:
            return Response(
                {
                    "message": "Validation error!!!!!!!!",
                    "error": str(e)
                }, status=status.HTTP_400_BAD_REQUEST
            )
        except Exception as e:
            return Response(
                {
                    "message": "Error Occurred..",
                    "error": str(e)
                }, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class Result(APIView):
    """
    For Retreving the result of voting held
    """

    def get(self, request, id):
        """
        For getting the result
        :param request:
        :param id: id of sprint
        :return: Response
        """
        try:
            votes = Votes.objects.filter(sprint_id=id)
            serializer = VoteSerializer(votes, many=True)
            list_of_votes = list()
            for vote_dic in serializer.data:
                vote_to = User.objects.get(id=vote_dic["vote_to"])

                list_of_votes.append(vote_to.username)
            vote_count = Counter(list_of_votes)
            winner = max(list_of_votes, key=list_of_votes.count)

            return Response(
                {
                    "winner": winner,
                    "vote Count": vote_count,
                    "vote details": serializer.data
                },
                status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {
                    "message": "Errror Occurred",
                    "error": str(e)
                }, status=status.HTTP_400_BAD_REQUEST
            )
