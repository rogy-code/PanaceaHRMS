from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from . models import Employee, Sallary, Department
from .forms import EmployeeForm


# Create your views here.
def home(request):
    employees = Employee.objects.all()
    departments = Department.objects.all()
    salarys = Sallary.objects.all()
    context = {'employees': employees,
               'departments': departments, 'salarys': salarys}
    return render(request, 'PanaceaApp/home.html', context)


def addEmployee(request):
    form = EmployeeForm()
    departments = Department.objects.all()

    if request.method == 'POST' and request.FILES:
        department_name = request.POST.get('department')
        department, create = Department.objects.get_or_create(
            name=department_name)

        Employee.objects.create(
            department=department,
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
        return redirect('home')

    context = {'form': form, 'departments': departments}
    return render(request, 'PanaceaApp/addEmployee.html', context)

@login_required(login_url='/login')
def employeeDetail(request, pk):
    employee = Employee.objects.get(id=pk)
    form = EmployeeForm(instance=employee)
    departments = Department.objects.all()
    

    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES, instance=employee)
        if form.is_valid():
            form.save()
            
            messages.success(request, 'employee updated!!!')
            return redirect('home')

    context = {'employee': employee, 'form': form, 'departments': departments}
    return render(request, 'PanaceaApp/employeeDetail.html', context)


def salary(request):
    salarys = Sallary.objects.all()
    context = {'salarys': salarys}
    return render(request, 'PanaceaApp/salary.html', context)


def salaryDetail(request, pk):
    salary = Sallary.objects.get(id=pk)
    employees = Employee.objects.all()
    context = {'salary': salary, 'employees': employees}
    return render(request, 'PanaceaApp/salaryDetail.html', context)


def addSalary(request):
    salarys = Sallary.objects.all()
    employees = Employee.objects.all()

    if request.method == 'POST':
        employee_name = request.POST.get('employee')
        employee, create = Employee.objects.get_or_create(
            fullname=employee_name)

        Sallary.objects.create(
            employee=employee,
            salary=request.POST.get('salary'),
            allowance=request.POST.get('allowance'),
            nssf=request.POST.get('nssf'),
            nhif=request.POST.get('nhif'),
        )
        messages.success(request, 'salary record added!!!')
        return redirect('salary')
    context = {'employees': employees, 'salarys': salarys}
    return render(request, 'PanaceaApp/addSalary.html', context)

def editSalary(request, pk):
    salary = Sallary.objects.get(id=pk)
    context = {'salary': salary}
    return render(request, 'PanaceaApp/editSalary.html', context)

def calender(request):
    context = {}
    return render(request, 'PanaceaApp/calender.html', context)
