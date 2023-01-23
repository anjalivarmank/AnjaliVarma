from django.db import models

# Create your models here.
class add_admindb(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    mobile = models.CharField(max_length=100, null=True, blank=True)
    password = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to="profile", null=True, blank=True)

class Categorydb(models.Model):
    Name = models.CharField(max_length=25, null=True, blank=True)
    Description = models.TextField(max_length=100,null=True, blank=True)
    Image = models.ImageField(upload_to="profile", null=True, blank=True)

class Products(models.Model):
    Name = models.CharField(max_length=25, null=True, blank=True)
    Price = models.IntegerField(null=True, blank=True)
    Published_Date = models.DateField(null=True, blank=True)
    author_name = models.CharField(max_length=250, null=True, blank=True)
    Image = models.ImageField(upload_to="profile", null=True, blank=True)
    Categry = models.CharField(max_length=20, null=True, blank=True)

class logindb(models.Model):
    username=models.CharField(max_length=100,null=True,blank=True)
    password=models.CharField(max_length=100,null=True,blank=True)

class emailsubdb(models.Model):
    email=models.EmailField(max_length=100,null=True,blank=True)

class messagedb(models.Model):
    name=models.CharField(max_length=100,null=True,blank=True)
    email=models.CharField(max_length=100,null=True,blank=True)
    subject=models.CharField(max_length=100,null=True,blank=True)
    message=models.CharField(max_length=100,null=True,blank=True)