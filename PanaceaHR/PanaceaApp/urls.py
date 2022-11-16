from django.urls import path
from  . import views
urlpatterns = [
    path('', views.home, name='home'),

    # employees urls
    path('addEmployee/', views.addEmployee, name='addEmployee'),
    path('employeedetail/<str:pk>/', views.employeeDetail, name='employeeDetail'),

    # salary urls
    path('salary/', views.salary, name='salary'),
    path('salaryDetail/<str:pk>/', views.salaryDetail, name='salaryDetail'),
    path('addSalary/', views.addSalary, name='addSalary'),
    path('editSalary/<str:pk>/', views.editSalary, name='editSalary'),
    path('deleteSalary/<str:pk>/', views.deleteSalary, name='deleteSalary'),

    # department urls
    path('department/', views.department, name='department'),
    path('createDepartment/', views.createDepartment, name='createDepartment'),
    path('editDepartment/<str:pk>/', views.editDepartment, name='editDepartment'),
    path('deleteDepartment/<str:pk>/', views.deleteDepartment, name='deleteDepartment'),

    # calender urls
    path('calender/', views.calender, name='calender'),
]