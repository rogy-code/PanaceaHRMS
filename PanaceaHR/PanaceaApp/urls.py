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

    # calender urls
    path('calender/', views.calender, name='calender'),
]