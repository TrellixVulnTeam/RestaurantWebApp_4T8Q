from django.contrib import admin
from .models import Business, BusinessUser, ProductsGroup, Product, Review
# Register your models here.

admin.site.register(BusinessUser)
admin.site.register(Business)
admin.site.register(ProductsGroup)
admin.site.register(Product)
admin.site.register(Review)