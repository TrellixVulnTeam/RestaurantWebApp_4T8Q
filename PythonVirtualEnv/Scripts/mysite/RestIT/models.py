from django.db import models
from django.utils import timezone

# Create your models here.
class CommonUserInfo(models.Model):
    login = models.CharField(max_length=20)
    password = models.CharField(max_length=30)
    signInDate = models.DateTimeField(default=timezone.now())
    lastLoginDate = models.DateTimeField(auto_now=True)
    avatar = models.ImageField()
    email = models.EmailField()
    address = models.TextField(max_length=100)
    
    class Meta:
        abstract = True

class BusinessUser(CommonUserInfo):
    ownerID = models.ManyToManyField("Business")
    permissions = models.CharField(max_length=20)

class Business(models.Model):
    owners = models.ManyToManyField("BusinessUser")
    businessName = models.CharField(max_length=40)
    address = models.TextField(max_length=100)
    description = models.TextField(max_length=100)
