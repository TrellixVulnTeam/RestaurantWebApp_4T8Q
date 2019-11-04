from django.contrib.auth.models import User
from .models.users.employee import Employee
from .models.users.company_owner import CompanyOwner
from .models.users.client import Client
from rest_framework import serializers
from .models.order_related_objects.company import Company
from .models.order_related_objects.order import Order


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    #is needed for inheritance in this case user
    username = serializers.CharField(read_only=True, source="user.username", default="None")
    workplace = serializers.CharField(default="None",read_only=True,source="company.name")
    orders_delivered = serializers.CharField(default="None",read_only=True, source="order.id")
    role = serializers.CharField(read_only=True, source="role.name")
    class Meta:
        #user = UserSerializer()
        model = Employee
        #fields = ['username', 'workplace', 'salary_per_month', 'birthday', 'orders_delivered','address', 'role']
        #fields ='__all__'

class CompanyOwnerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CompanyOwner
        fields = ['address']

class ClientSerializer(serializers.HyperlinkedModelSerializer): 
    username = serializers.CharField(read_only=True, source="user.username")
    class Meta:
        model = Client
        fields = ['username']

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'