from django.db import models
from django.utils import timezone
import datetime
from django.contrib.auth.models import User
from BasicBusinessManager.models.order_related_objects.company import Company
from BasicBusinessManager.models.order_related_objects.order import Order
# Create your models here.
class Employee(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    workplace = models.ManyToManyField("Company")
    years_employed = models.DateField()
    salary_per_month = models.DecimalField(decimal_places =2,max_digits=10)
    birthsday = models.DateField(default=timezone.now)
    orders_delivered = models.ManyToManyField("Order",blank=True)
    address = models.CharField(max_length=60,blank=True)
    role = models.ForeignKey("Role",on_delete=models.DO_NOTHING,blank=True,default=1)

    def years_employed(self):
        self.years_employed = timezone.now() - self.date_joined
        return self.years_employed

    def __str__(self):
        try:
            return self.first_name
        except: 
            return self.username

class Role(models.Model):
    name = models.CharField(max_length=30)
    responsibilities = models.CharField(max_length=300,blank=True)

    def __str__(self):
        return self.name