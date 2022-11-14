from django.shortcuts import render
from django.contrib import messages
from . models import Employee,Sallary,Department
from .forms import AddEmployeeForm

# Create your views here.
def home(request):
    employees = Employee.objects.all()
    departments = Department.objects.all()
    context = {'employees': employees, 'departments': departments}
    return render(request, 'PanaceaApp/home.html', context)

def addEmployee(request):
    form = AddEmployeeForm()
    if request.method == 'POST' and request.FILES:
        Employee.objects.create(
            fullname=request.POST.get('fullname'),
            email=request.POST.get('email'),
            telephone=request.POST.get('telephone'),
            idnumber=request.POST.get('idnumber'),
            position=request.POST.get('position'),
            gender=request.POST.get('gender'),
            dateofbirth=request.POST.get('dateofbirth'),
            idphoto=request.FILES['idphoto'],
            nhifphoto=request.FILES['nhifphoto'],
            nssfphoto=request.FILES['nssfphoto'],
        )
        messages.success(request, 'user added!!!')
    context = {'form': form}
    return render(request, 'PanaceaApp/addEmployee.html', context)

def employeeDetail(request, pk):
    employee = Employee.objects.get(id=pk)
    employees = Employee.objects.all()
    context = {'employee': employee, 'employees': employees}
    return render(request, 'PanaceaApp/employeeDetail.html', context)

def salary(request):
    salarys = Sallary.objects.all()
    context = {'salarys': salarys}
    return render(request, 'PanaceaApp/salary.html', context)

def salaryDetail(request,pk):
    salary = Sallary.objects.get(id=pk)
    employees = Employee.objects.all()
    context = {'salary': salary, 'employees': employees}
    return render(request, 'PanaceaApp/salaryDetail.html', context)

def addSalary(request):
    salarys = Sallary.objects.all()
    employees = Employee.objects.all()

    if request.method == 'POST':
        employee_name = request.POST.get('employee')
        employee, create = Employee.objects.get_or_create(fullname=employee_name)

        Sallary.objects.create(
            employee=employee,
            salary=request.POST.get('salary'),
            allowance=request.POST.get('allowance'),
            nssf=request.POST.get('nssf'),
            nhif=request.POST.get('nhif'),
        )
        messages.success(request, 'salary record added!!!')
    context = {'employees': employees, 'salarys': salarys}
    return render(request, 'PanaceaApp/addSalary.html', context)


def calender(request):
    context = {}
    return render(request, 'PanaceaApp/calender.html', context)