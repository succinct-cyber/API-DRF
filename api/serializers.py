from rest_framework import serializers
from cadence.models import Cadence
from employees.models import Employee

class CadenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cadence
        fields = "__all__" 



class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"

        