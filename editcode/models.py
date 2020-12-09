from django.db import models

# Create your models here.

from django.contrib import admin


class User(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

class Code(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=3)
    file_name = models.CharField(max_length=200)
    text = models.CharField(max_length=2000, default="")

admin.site.register(User)
admin.site.register(Code)

