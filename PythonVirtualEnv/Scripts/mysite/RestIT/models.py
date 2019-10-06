from django.db import models
from django.utils import timezone

# Create your models here.
class CommonUserInfo(models.Model):
    login = models.CharField(max_length=20)
    password = models.CharField(max_length=30)
    signInDate = models.DateTimeField(default=timezone.now())
    lastLoginDate = models.DateTimeField(auto_now=True)
    avatar = models.ImageField(blank=True)
    email = models.EmailField()
    address = models.TextField(max_length=100,blank=True)
    name = models.TextField(max_length=30,default="John")
    surname = models.TextField(max_length=30,default="Kennedy")
    def __str__(self):
        return self.name + " " + self.surname
    
    class Meta:
        abstract = True

class BusinessUser(CommonUserInfo):
    ownerID = models.ManyToManyField("Business",blank=True)
    permissions = models.CharField(max_length=20,blank=True)

class Business(models.Model):
    owners = models.ManyToManyField("BusinessUser")
    businessName = models.CharField(max_length=40)
    address = models.TextField(max_length=100)
    description = models.TextField(max_length=100,blank=True)
    def __str__(self):
        return self.businessName
