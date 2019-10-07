from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator

# Create your models here.
class CommonUserInfo(models.Model):
    login = models.CharField(max_length=20,blank=True,unique=True)
    password = models.CharField(max_length=30,blank=True)
    signUpDate = models.DateTimeField(default=timezone.now())
    lastLoginDate = models.DateTimeField(auto_now=True)
    avatar = models.ImageField(blank=True)
    email = models.EmailField(default="xyz@gmail.com")
    address = models.TextField(max_length=100,blank=True)
    firstName = models.TextField(max_length=30,default="John")
    lastName = models.TextField(max_length=30,default="Kennedy")
    def __str__(self):
       return self.firstName + " " + self.lastName
    
    class Meta:
        abstract = True

class BusinessUser(CommonUserInfo):
    ownerID = models.ManyToManyField("Business",blank=True)
    permissions = User.user_permissions

class Business(models.Model):
    owners = models.ManyToManyField("BusinessUser",blank=True)
    businessName = models.CharField(default="My business",max_length=40)
    address = models.TextField(max_length=100,blank=True)
    description = models.TextField(max_length=100,blank=True)
    def __str__(self):
        return self.businessName

class BasicDetails(models.Model):
    name = models.CharField(max_length=30,blank=True)
    def __str__(self):
        return self.name
    class Meta:
        abstract = True

class Product(BasicDetails):
    name = models.CharField(max_length=30,blank=True, default="Product")
    group = models.ManyToManyField("ProductsGroup",max_length=30)
    price = models.DecimalField(default=0.00,max_digits=100,decimal_places=2)
    notes = models.CharField(blank=True,max_length=300)
    rating = models.DecimalField(default=0,max_digits=3,decimal_places=2)

class Review(BasicDetails):
    title = models.CharField(max_length=30,default="Review")
    details = models.CharField(max_length=500)
    rate = models.PositiveIntegerField(validators=[MaxValueValidator(5)])
    reviewedProduct=models.ForeignKey("Product", on_delete=models.CASCADE)

class ProductsGroup(BasicDetails):
    notes = models.CharField(blank=True,max_length=500)