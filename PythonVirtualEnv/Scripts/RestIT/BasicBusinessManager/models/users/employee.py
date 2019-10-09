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
    years_employed = models.DateTimeField()
    salary_per_month = models.DecimalField(decimal_places =2,max_digits=10)
    birthsday = models.DateTimeField(default=timezone.now)
    orders_delivered = models.ManyToManyField("Order")
    address = models.CharField(max_length=60,blank=True)
    role = models.ForeignKey("Role",on_delete=models.DO_NOTHING,blank=True,default=1)

    def years_employed(self,years_employed):
        self.years_employed= timezone.now - self.user.date_joined
    def __str__(self):
        return self.user.name


class Role(models.Model):
    name = models.CharField(max_length=30)
    responsibilities = models.CharField(max_length=300,blank=True)

    def __str__(self):
        return self.name