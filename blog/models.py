# from django.db import models

# Create your models here.
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class Post(models.Model):
    body = RichTextUploadingField(blank=True,
                                    config_name='special')