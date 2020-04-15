from rest_framework import serializers


from .models import EmployeeModel


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EmployeeModel
        fields = ('email', 'first_name', 'last_name', 'url')
