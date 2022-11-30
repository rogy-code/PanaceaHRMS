from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from . models import Employee, Sallary, Department
from .forms import EmployeeForm, salaryForm
from django.contrib.auth import authenticate, login, logout


# dashboard views
def home(request):
    employees = Employee.objects.all()
    departments = Department.objects.all()
    salarys = Sallary.objects.all()
   
    
    context = {'employees': employees, 'departments': departments, 'salarys': salarys}
    return render(request, 'PanaceaApp/home.html', context)

# employee login
def empLogin(request):
    if request.method == 'POST':
        email = request.POST.get('email').lower()
        idnumber = request.POST.get('idnumber')

        try:
            employee = Employee.objects.get(email=email)
            employee = Employee.objects.get(idnumber=idnumber)

        except:
            messages.error(request, 'Invalid login credentials')
            Employee = authenticate(email=email, idnumber=idnumber)
        
        if employee is not None:
            login(request, employee)
            return redirect("home")
        else:
            messages.error(request, 'Invalid login credentials')
            return redirect('login')
    context = {}
    return render(request, 'PanaceaApp/empLogin.html', context)


# add employee record
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

# select employee by id and edit/update
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

# salary
def salary(request):
    salarys = Sallary.objects.all()
    context = {'salarys': salarys}
    return render(request, 'PanaceaApp/salary.html', context)

# payslip
def payslip(request, pk):
    salary = Sallary.objects.get(id=pk)
    employees = Employee.objects.all()
    context = {'salary': salary, 'employees': employees}
    return render(request, 'PanaceaApp/payslip.html', context)

# salary select by is
def salaryDetail(request, pk):
    salary = Sallary.objects.get(id=pk)
    employees = Employee.objects.all()
    context = {'salary': salary, 'employees': employees}
    return render(request, 'PanaceaApp/salaryDetail.html', context)

# add salary record
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
        )
        messages.success(request, 'salary record added!!!')
        return redirect('salary')
    context = {'employees': employees, 'salarys': salarys}
    return render(request, 'PanaceaApp/addSalary.html', context)

# edit dalary record
def editSalary(request, pk):
    salary = Sallary.objects.get(id=pk)
    form = salaryForm(instance=salary)

    if request.method == 'POST':
        salary.salary = request.POST.get('salary')
        salary.allowance = request.POST.get('allowance')
        salary.save()
        messages.success(request, 'salary updated!!!')
        return redirect('salary')

    context = {'salary': salary, 'form': form}
    return render(request, 'PanaceaApp/editSalary.html', context)

# delete salary records
@login_required(login_url='/login')
def deleteSalary(request, pk):
    salary = Sallary.objects.get(id=pk)

    if request.method == 'POST':
        salary.delete()
        messages.warning(request, 'Room deleted')
        return redirect('home')
    return render(request, 'PanaceaApp/delete.html', {'obj': salary})


# department views
def department(request):
    departments = Department.objects.all()
    context = {'departments': departments}
    return render(request, 'PanaceaApp/department.html', context)

# create department views
def createDepartment(request):
    departments = Department.objects.all()

    if request.method == 'POST':
        Department.objects.create(
            name=request.POST.get('name'),
            history=request.POST.get('history')
        )
        messages.success(request, 'department added!!!')
        return redirect('department')
    context = {'departments': departments}
    return render(request, 'PanaceaApp/createDepartment.html', context)

# edit department views
def editDepartment(request, pk):
    department = Department.objects.get(id=pk)

    if request.method == 'POST':
        department.name = request.POST.get('name')
        department.history = request.POST.get('history')
        department.save()
        messages.success(request, 'salary updated!!!')
        return redirect('department')

    context = {'department': department}
    return render(request, 'PanaceaApp/editDepartment.html', context)

# delete department records
@login_required(login_url='/login')
def deleteDepartment(request, pk):
    department = Department.objects.get(id=pk)

    if request.method == 'POST':
        department.delete()
        messages.warning(request, 'department deleted')
        return redirect('department')

    context = {'obj': department}
    return render(request, 'PanaceaApp/delete.html', context)

@login_required(login_url='/login')
def deleteEmployee(request, pk):
    employee = Employee.objects.get(id=pk)

    if request.method == 'POST':
        employee.delete()
        messages.warning(request, 'employeee deleted')
        return redirect('home')

    context = {'obj': employee}
    return render(request, 'PanaceaApp/delete.html', context)


def calender(request):
    context = {}
    return render(request, 'PanaceaApp/calender.html', context)