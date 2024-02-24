from django.contrib import admin

from .models import Comment, CustomUser, Image, Task

# Register your models here.


admin.site.register(CustomUser)
admin.site.register(Task)
admin.site.register(Comment)
admin.site.register(Image)
