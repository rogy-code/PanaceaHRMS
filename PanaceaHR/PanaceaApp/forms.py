from django.forms import ModelForm
from .models import Employee
from django.forms import ModelForm, TextInput

 
class AddEmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        exclude = ['created','updated']

class updateEmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        exclude = ['created','updated']
       