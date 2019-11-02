from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class CompanyManager(models.Manager):
    def create_owner(self,user):
        owner = self.create(user=user)
        return owner
class CompanyOwner(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    company_owned = models.ManyToManyField("Company",blank=True)
    address = models.CharField(max_length=60,blank=True)
    objects = CompanyManager()
    def __str__(self):
        return self.user.username
    def type_name(self):
        return "CompanyOwner"