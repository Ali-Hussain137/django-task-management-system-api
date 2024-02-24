import cloudinary.models
from django.db import models

from . import Comment, Task


class Image(models.Model):
    image = cloudinary.models.CloudinaryField("image")
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, null=True)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, null=True)
