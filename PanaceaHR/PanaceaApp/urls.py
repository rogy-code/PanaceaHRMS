from django.urls import path
from  . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('addEmployee/', views.addEmployee, name='addEmployee'),
    path('employeedetail/<str:pk>/', views.employeeDetail, name='employeeDetail'),
    path('salary/', views.salary, name='salary'),
    path('salaryDetail/<str:pk>/', views.salaryDetail, name='salaryDetail'),
    path('addSalary/', views.addSalary, name='addSalary'),
    path('editSalary/<str:pk>/', views.editSalary, name='editSalary'),
    path('calender/', views.calender, name='calender'),
]