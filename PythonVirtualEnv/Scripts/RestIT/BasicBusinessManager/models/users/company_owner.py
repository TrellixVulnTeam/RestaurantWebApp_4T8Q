from django.db import models
from BasicBusinessManager.models.order_related_objects.company import Company
# Create your models here.
class CompanyOwner(models.Model):
    user = models.OneToOneField("User",on_delete=models.CASCADE)
    company_owned = models.ManyToManyField("Company")
    address = models.CharField(max_length=60,blank=True)