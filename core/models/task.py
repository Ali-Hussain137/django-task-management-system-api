from datetime import date

from django.core.exceptions import ValidationError
from django.db import models

from . import CustomUser


class Task(models.Model):

    class StatusChoiceForStatus(models.TextChoices):
        OPTION1 = "pending", "Pending"
        OPTION2 = "in process", "In Process"
        OPTION3 = "completed", "Completed"

    class StatusChoiceForApproval(models.TextChoices):
        OPTION1 = "pending", "Pending"
        OPTION2 = "approved", "Approved"
        OPTION3 = "rejected", "Rejected"

    title = models.CharField(max_length=255)
    description = models.TextField(max_length=1000, null=True, blank=True)
    deadline = models.DateField(null=False)
    status = models.CharField(
        max_length=10,
        choices=StatusChoiceForStatus.choices,
        default=StatusChoiceForStatus.OPTION1,
    )
    approval = models.CharField(
        max_length=10,
        choices=StatusChoiceForApproval.choices,
        default=StatusChoiceForApproval.OPTION1,
    )
    upload_file = models.FileField(upload_to="uploads/", null=True)
    assigner = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="assigner"
    )
    performer = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="performer"
    )

    def clean(self):
        if self.deadline and self.deadline < date.today():
            raise ValidationError({"date_field": "Date cannot be negative."})
