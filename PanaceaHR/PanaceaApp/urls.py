from django.urls import path
from  . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('addEmployee/', views.addEmployee, name='addEmployee'),
    path('employeedetail/<str:pk>/', views.employeeDetail, name='employeeDetail'),
    path('calender/', views.calender, name='calender'),
]