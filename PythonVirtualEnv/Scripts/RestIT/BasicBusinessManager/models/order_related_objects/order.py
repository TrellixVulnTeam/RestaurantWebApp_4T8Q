from django.db import models
from django.utils import timezone
import datetime
from .company import Company
from django.core.exceptions import ValidationError

# Create your models here.

# Don't allow dates older than order_date.
class Order(models.Model):
    client = models.OneToOneField("Client",on_delete=models.DO_NOTHING,blank=True)
    products = models.ManyToManyField("Product")
    deliverant = models.OneToOneField("Company",on_delete=models.DO_NOTHING)
    order_date = models.DateTimeField(auto_now=True)
    delivery_date = models.DateTimeField(blank = True)
    address_of_delivery = models.CharField(max_length=60,blank=True)
    notes = models.CharField(max_length=100)
    delivered = models.BooleanField(default=False)

    def was_delivered(self):
        return timezone.now() > self.deliver_date >= self.order_date
        
    was_delivered.admin_order_field = delivered
    was_delivered.short_desction = "Delivered ?"

