from django.db import models
from BasicBusinessManager.models.users.company_owner import CompanyOwner

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=30)
    businesses_owner = models.ManyToManyField("CompanyOwner")
    address = models.CharField(max_length=60,blank=True)
    sector = models.ManyToManyField("Sector")

class Sector(models.Model):
    name = models.CharField(max_length=30)
    decription = models.CharField(max_length=300)
    companys_in_sector = models.ManyToManyField("Company")