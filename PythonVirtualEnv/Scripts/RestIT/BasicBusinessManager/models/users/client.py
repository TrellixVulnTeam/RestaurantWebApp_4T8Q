from django.db import models
import datetime
from django.core.validators import MaxValueValidator
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class ClientManager(models.Manager):
    def create_client(self,user):
        client = self.create(user=user)
        return client

class Client(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    birthsday = models.DateTimeField(default=timezone.now)
    discount = models.PositiveIntegerField(validators=[MaxValueValidator(100)],default=0)
    address = models.CharField(max_length=60,blank=True)
    objects = ClientManager()
    def __str__(self):
        return self.user.username
