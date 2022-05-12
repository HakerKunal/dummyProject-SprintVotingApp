from rest_framework import serializers
from .utils import InsertionError
from .models import Sprint


class SprintSerializer(serializers.Serializer):
    """
    Serializer is used to converting the python object for the Sprint
    """
    id = serializers.IntegerField(required=False)
    sprint_name = serializers.CharField(required=False)
    start_date = serializers.DateField(required=False)
    end_date = serializers.DateField(required=False)
    is_active = serializers.BooleanField(default=True, required=False)

    def create(self, validate_data):
        """
        for creating the sprint
        :param validate_data:  validate the api data
        :return: sprint
        """
        sprint = Sprint.objects.filter(is_active=True)
        if not sprint:
            sprint = Sprint.objects.create(
                sprint_name=validate_data.get("sprint_name"),
                start_date=validate_data.get("start_date"),
                end_date=validate_data.get("end_date"),
            )
            return sprint
        else:
            raise InsertionError("One Sprint is already Active")

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.id = validated_data.get('id', instance.id)
        instance.sprint_name = validated_data.get('sprint_name', instance.sprint_name)
        instance.start_date = validated_data.get('start_date', instance.start_date)
        instance.end_date = validated_data.get('end_date', instance.end_date)
        instance.is_active = validated_data.get('is_active', instance.is_active)

        instance.save()
        return instance
