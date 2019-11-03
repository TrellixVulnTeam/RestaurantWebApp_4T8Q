from django.contrib.auth.models import User
from .models.users.employee import Employee
from .models.users.company_owner import CompanyOwner
from .models.users.client import Client
from rest_framework import serializers


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    #is needed for inheritance in this case user
    username = serializers.CharField(read_only=True, source="user.username")
    class Meta:
        #user = UserSerializer()
        model = Employee
        #fields = ['user', 'workplace', 'years_employed', 'salary_per_month', 'birthday', 'orders_delivered','address', 'role']
        fields =['username']
        
        #jutro zrobić REST
    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Snippet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance
class CompanyOwnerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CompanyOwner
        fields = ['url', 'name']

class ClientSerializer(serializers.HyperlinkedModelSerializer): 
    username = serializers.CharField(read_only=True, source="user.username")
    class Meta:
        model = Client
        fields = ['username']