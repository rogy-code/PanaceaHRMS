from django.forms import ModelForm
from .models import Employee, Sallary
from django import forms
 
class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        exclude = ['created','updated']

class salaryForm(ModelForm):
    class Meta:
        model = Sallary
        fields = '__all__' 