from rest_framework import serializers
from employee.models import Beneficiary, Employee

class BeneficiatySerializer(serializers.ModelSerializer):

    class Meta:
        model = Beneficiary
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    beneficiary = BeneficiatySerializer()
    photo = serializers.ImageField(required=True)

    class Meta:
        model = Employee
        fields = [
            'id', 
            'name',
            'email',
            'position',
            'salary',
            'status',
            'date_of_hire',
            'photo',
            'beneficiary'
        ]

class CreateEmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = (
            'name', 
            'email',
            'position',
            'salary',
            'status',
            'date_of_hire',
            'photo',
            'beneficiary'
        )