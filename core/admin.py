from django.contrib import admin
from .models import CustomUser, Task, Comment
# Register your models here.


admin.site.register(CustomUser)
admin.site.register(Task)
admin.site.register(Comment)
