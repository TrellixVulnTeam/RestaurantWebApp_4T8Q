from django.db import models
from django.utils import timezone
import datetime
from BasicBusinessManager.models.order_related_objects.company import Company
from BasicBusinessManager.models.order_related_objects.order import Order
# Create your models here.
class Employee(models.Model):
    user = models.OneToOneField("User",on_delete=models.CASCADE)
    workplace = models.ManyToManyField("Company")
    years_employed = models.DateTimeField()
    salary_per_month = models.DecimalField(decimal_places =2,max_digits=10)
    birthsday = models.DateTimeField(default=timezone.now)
    orders_delivered = models.ManyToManyField("Order")
    address = models.CharField(max_length=60,blank=True)

    def years_employed(self,years_employed):
        self.years_employed= timezone.now - self.user.date_joined
