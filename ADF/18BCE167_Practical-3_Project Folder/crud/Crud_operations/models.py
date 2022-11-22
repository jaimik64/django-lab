from django.db import models

Institute=(('itnu','ITNU'),('imnu','IMNU'),('icnu','ICNU'),('ilnu','ILNU'),('ipnu','IPNU'))
gender=(('male','Male'),('female','Female'))

# Create your models here.
class CRUD(models.Model):
    # pass
    First_Name=models.CharField(max_length=50)
    Middle_Name=models.CharField(max_length=50)
    Last_Name=models.CharField(max_length=50)
    Age=models.IntegerField(default=0)
    Gender=models.CharField(max_length=10,choices=gender,default='male')
    Address=models.CharField(max_length=100,default="")
    Emai_Id=models.EmailField()
    Mobile_Number=models.IntegerField()
    Alternate_Email_Id=models.EmailField()
    Alternate_Mobile_Number=models.IntegerField()
    Father_Name=models.CharField(max_length=50)
    Mother_Name=models.CharField(max_length=50)
    Institute_Name=models.CharField(max_length=10,choices=Institute,default='imnu') 
    Branch_Name=models.CharField(max_length=50)
