import json

from django.db import models 

from django.utils import timezone
from datetime import datetime
 
 

class EmployeeTable(models.Model):
    gs_empid = models.AutoField(db_column='gs_empid', primary_key=True)
    gs_empfirstname = models.CharField(max_length=100, db_column='gs_empfirstname')
    gs_emplastname = models.CharField(max_length=100, db_column='gs_emplastname')
    gs_empdob = models.DateTimeField(db_column='gs_empdob')
    gs_gender = models.CharField(max_length=100, db_column='gs_gender')
    gs_value = models.TextField(db_column='gs_value', blank = True) 
    is_active = models.CharField(db_column='is_active',  default='N', max_length=10, choices=((1, "Y"), (2, "N")), help_text="'Y' or 'N'")
    create_at = models.DateTimeField(db_column='create_at', default=timezone.now) 
    status    = models.CharField(max_length=100, db_column='status')

    def __str__(self):
        role_data = {}
        role_data['gs_empid'] = self.gs_empid
        role_data['gs_empfirstname'] = self.gs_empfirstname
        role_data['gs_emplastname'] = self.gs_emplastname
        role_data['gs_empdob'] = str(self.gs_empdob)
        role_data['gs_gender'] = self.gs_gender
        role_data['gs_value'] = self.gs_value
        role_data['is_active'] = self.is_active
        role_data['create_at'] = str(self.create_at)
        role_data['status'] = self.status

        return json.dumps(role_data)
 
    
    class Meta:
        db_table = "EMPLOYE_RECORD"

