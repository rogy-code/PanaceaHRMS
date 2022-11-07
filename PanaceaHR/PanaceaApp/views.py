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

def employeeDetail(request, pk):
    employee = Employee.objects.get(id=pk)
    employees = Employee.objects.all()
    context = {'employee': employee, 'employees': employees}
    return render(request, 'PanaceaApp/employeeDetail.html', context)

def calender(request):
    context = {}
    return render(request, 'PanaceaApp/calender.html', context)