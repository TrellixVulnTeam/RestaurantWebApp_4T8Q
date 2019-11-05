from django.contrib.auth.models import User
from .models.order_related_objects.company import Company, Sector
from .models.order_related_objects.order import Order
from .models.users.employee import Employee, Role
from .models.users.company_owner import CompanyOwner
from .models.users.client import Client
from .models.order_related_objects.product import Product
from .models.order_related_objects.sale_out import Sale_out

from rest_framework import serializers


class EmployeeSerializer(serializers.ModelSerializer):
    #is needed for inheritance in this case user
    username = serializers.ReadOnlyField(read_only=True, source="user.username")
    workplace = serializers.ReadOnlyField(read_only=True, source="company.name")
    orders_delivered = serializers.PrimaryKeyRelatedField(many=True, queryset=Order.objects.all())
    role = serializers.ReadOnlyField(read_only=True, source="role.name")
    class Meta:
        #user = UserSerializer()
        model = Employee
        #fields = ['username', 'workplace', 'salary_per_month', 'birthday', 'orders_delivered','address', 'role']
        fields = '__all__'

class CompanyOwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyOwner
        fields = '__all__'

class ClientSerializer(serializers.ModelSerializer): 
    username = serializers.CharField(read_only=True, source="user.username")
    class Meta:
        model = Client
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class SaleOutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale_out
        fields = '__all__'

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'
        
class SectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sector
        fields = '__all__'

