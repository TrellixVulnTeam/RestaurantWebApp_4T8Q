from django.db import models

# Create your models here.
class Order(models.Model):
    date = models.DateTimeField(auto_now=True)
    #products = models.ManyToManyField("Product")
