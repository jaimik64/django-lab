from django.contrib.auth.models import User
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import OneToOneField

# Create your models here.
class Login(models.Model):
    pass
    # username=models.CharField(max_length=15)
    # password=models.CharField(max_length=50)
    # emailId=models.EmailField()

class UserExtraData(models.Model):
    user=OneToOneField(User,on_delete=models.CASCADE)
    birthDate=models.DateField()
    age=models.IntegerField()
    mobileNo=models.IntegerField()
    gender=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    pincode=models.IntegerField()
    state=models.CharField(max_length=50)
    
