from rest_framework import serializers
from .models import Company, Employee


class CompanySerializers(serializers.ModelSerializer):
    class Meta:
        model = Company  # Specify the model that the serializer should be based on
        fields = '__all__'  # You can also specify a list of fields if you don't want to include all fields


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
