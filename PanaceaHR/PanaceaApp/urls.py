from django.urls import path
from  . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('addEmployee/', views.addEmployee, name='addEmployee'),
]