from .utils import InsertionError

from django.db import models


class Sprint(models.Model):
    sprint_name = models.CharField(max_length=165, unique=True, null=False)
    start_date = models.DateField()
    end_date = models.DateField()
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if self.start_date < self.end_date:

            super().save()
        else:
            raise InsertionError("end date should be greater than start date")


class Parameter(models.Model):
    parameter_name = models.CharField(max_length=35, unique=True)
