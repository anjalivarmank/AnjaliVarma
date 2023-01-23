from django.db import models

# Create your models here.
class signupdb(models.Model):
    name=models.CharField(max_length=100,null=True,blank=True)
    password=models.CharField(max_length=100,null=True,blank=True)
    conformpassword=models.CharField(max_length=1000,null=True,blank=True)

class cartdb(models.Model):
    Name=models.CharField(max_length=100,null=True,blank=True)
    Quantity=models.IntegerField(null=True,blank=True)
    Author=models.CharField(max_length=100,null=True,blank=True)
    Total=models.IntegerField(null=True,blank=True)



