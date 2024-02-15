from django.core.exceptions import ValidationError
from django.db import models

from . import CustomUser


class Task(models.Model):

    class StatusChoice(models.TextChoices):
        OPTION1 = "pending", "Pending"
        OPTION2 = "in process", "In Process"
        OPTION3 = "completed", "Completed"

    title = models.CharField(max_length=255)
    description = models.TextField(max_length=1000, null=True, blank=True)
    deadline = models.DateField(null=False)
    status = models.CharField(
        max_length=10, choices=StatusChoice.choices, default=StatusChoice.OPTION1
    )
    approved = models.BooleanField(default=False)
    upload_file = models.FileField(upload_to="uploads/")
    assigner = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="assigner"
    )
    performer = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="performer"
    )

    def clean(self):
        if self.deadline and self.deadline < models.DateField().default:
            raise ValidationError({"date_field": "Date cannot be negative."})
