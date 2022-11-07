from django.shortcuts import render
from . models import Employee

# Create your views here.
def home(request):
    employees = Employee.objects.all()
    context = {'employees': employees}
    return render(request, 'PanaceaApp/home.html', context)

def addEmployee(request):
    context = {}
    return render(request, 'PanaceaApp/addEmployee.html', context)