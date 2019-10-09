from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator
import datetime
from .product import Product
# Create your models here.
class Sale_out(models.Model):
    name = models.CharField(max_length=30,blank=True)
    discount = models.PositiveIntegerField(max_digits=3,validators=[MaxValueValidator(100)])
    products = models.ManyToManyRel("Product")
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    def finished(self):
        return timezone.now - self.end_date > 0
