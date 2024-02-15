import cloudinary.models
from django.db import models

from . import Comment, CustomUser, Task


class Image(models.Model):
    image = cloudinary.models.CloudinaryField("image")
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
