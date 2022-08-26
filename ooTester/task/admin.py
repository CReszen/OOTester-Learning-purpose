from django.contrib import admin
from .models import Question, UserDB

# Register your models here.
admin.site.register(Question)
admin.site.register(UserDB)
