from django.db import models
from django.utils.html import mark_safe
# Create your models here.

class Posts(models.Model):
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    like = models.IntegerField(max_length=10, default=0, editable=False)
    dislike = models.IntegerField(max_length=10, default=0, editable=False)
    image = models.ImageField(max_length=200, upload_to='uploads/')