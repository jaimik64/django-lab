from django.db import models

# Create your models here.

class Post(models.Model):
    id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=50)
    post=models.TextField()
    title=models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')
    file = models.FileField(upload_to='files/')