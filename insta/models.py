from django.db import models
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
# import mysql.connector


# Create your models here.
class Time(models.Model):
    from_time = models.CharField(max_length=200, default=None)
    to_time = models.CharField(max_length=200, default=None)
    user_email = models.CharField(max_length=200, default=None)

class Setting(models.Model):
    username = models.CharField(max_length=200, default=None)
    insta_id = models.CharField(max_length=200, default=None)
    insta_pass = models.CharField(max_length=200, default=None)
    status = models.CharField(max_length=200, default="off")

class Details(models.Model):
    user_email = models.CharField(max_length=200 ,default=None )

    account=models.CharField(max_length=200 ,default=None )
   
class Comments(models.Model):
    user_email = models.CharField(max_length=100,default="None" )
    comment = models.CharField(max_length=200,default=None )

class Settings(models.Model):
    user_email = models.CharField(max_length=200 )
    status=models.CharField(max_length=200 ,default='off')