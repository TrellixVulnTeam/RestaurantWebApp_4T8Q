from django.db import models
import datetime
from django.core.validators import MaxValueValidator
from django.utils import timezone
# Create your models here.
class Client(models.Model):
    user = models.OneToOneField("User",on_delete=models.CASCADE)
    birthsday = models.DateTimeField(default=timezone.now)
    orders = models.ManyToManyField("Orders")
    discount = models.PositiveIntegerField(max_length=3,validators=[MaxValueValidator(100)])
    address = models.CharField(max_length=60,blank=True)
