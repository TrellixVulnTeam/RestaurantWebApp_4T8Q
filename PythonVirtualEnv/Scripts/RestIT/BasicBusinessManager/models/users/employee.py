from django.db import models
from django.utils import timezone
import datetime
from django.contrib.auth.models import User
from BasicBusinessManager.models.order_related_objects.company import Company
from BasicBusinessManager.models.order_related_objects.order import Order
# Create your models here.

class EmployeeManager(models.Manager):
    def create_employee(self,user):
        employee = self.create(user=user)
        return employee

class Employee(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    workplace = models.ManyToManyField("Company",blank=True)
    years_employed = models.DateField()
    salary_per_month = models.DecimalField(decimal_places =2,max_digits=10,default=0.00)
    birthsday = models.DateField(default=timezone.now)
    orders_delivered = models.ManyToManyField("Order",blank=True)
    address = models.CharField(max_length=60,blank=True)
    role = models.ForeignKey("Role",on_delete=models.DO_NOTHING,blank=True, null=True)
    objects = EmployeeManager()

    def years_employed(self):
        self.years_employed = timezone.now() - self.date_joined
        return self.years_employed

    def __str__(self):
        try:
            if self.user.first_name != "":
                return self.user.first_name
            else:
                return self.user.username
        except: 
            return self.user.username

class Role(models.Model):
    name = models.CharField(max_length=30)
    responsibilities = models.CharField(max_length=300,blank=True)

    def __str__(self):
        return self.name