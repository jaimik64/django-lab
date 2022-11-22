import datetime
from django.db import models

# Create your models here.
class User(models.Model):
    CHOICE = (
        ("Male", "Male"),
        ("Female", "Female")
    )

    name = models.CharField(max_length=250)
    email = models.EmailField()
    password = models.CharField(max_length=18)
    phone = models.CharField(max_length=200)
    username = models.CharField(max_length=20)
    birthdate = models.DateField("Date",default=datetime.date.today())
    gender = models.CharField(choices=CHOICE, max_length=100)
    is_active = models.IntegerField(
        default = 1,
        blank = True,
        null = True,
        help_text='1->active, 0->inactive',
        choices =((1, 'active'), (0,'inactive'))
    )

# class Comments(models.Model):
    