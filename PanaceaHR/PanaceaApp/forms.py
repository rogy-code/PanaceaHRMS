from django.forms import ModelForm
from .models import Employee
 
class AddEmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        exclude = ['created','updated']