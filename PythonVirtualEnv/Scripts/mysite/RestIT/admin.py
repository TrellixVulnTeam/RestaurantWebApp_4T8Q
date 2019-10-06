from django.contrib import admin
from .models import Business, BusinessUser
# Register your models here.

admin.site.register(BusinessUser)
admin.site.register(Business)