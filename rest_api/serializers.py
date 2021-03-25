import datetime

from rest_framework import serializers

from .models import *

class EmployeeTableSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = EmployeeTable
        fields = ('gs_empid', 'gs_empfirstname', 'gs_emplastname','gs_empdob','gs_gender','gs_value', 'is_active', 'create_at', 'status')

