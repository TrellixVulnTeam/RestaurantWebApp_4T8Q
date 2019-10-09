from django.db import models
from django.utils import timezone
import datetime
from .company import Company

# Create your models here.
class Order(models.Model):
    client = models.OneToOneField("Client",on_delete=models.DO_NOTHING)
    products = models.ManyToManyField("Product")
    deliverant = models.OneToOneField("Company",on_delete=models.DO_NOTHING)
    order_date = models.DateTimeField(auto_now=True)
    deliver_date = models.DateTimeField(blank = True)
    price = models.DecimalField(max_digits=20,decimal_places=2)
    address_of_delivery = models.CharField(max_length=60,blank=True)
    notes = models.CharField(max_length=100)
