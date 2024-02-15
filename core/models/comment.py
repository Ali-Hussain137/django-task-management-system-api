from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _

from . import CustomUser, Task


def validate_not_empty_or_whitespace(value):
    if not value.strip():
        raise ValidationError(
            _("This field cannot be empty or contain only whitespace.")
        )


class Comment(models.Model):
    comment = models.CharField(
        max_length=255, validators=[validate_not_empty_or_whitespace]
    )
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
