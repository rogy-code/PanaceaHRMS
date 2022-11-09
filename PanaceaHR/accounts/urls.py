from django.urls import path
from  . import views
urlpatterns = [
    path('', views.loginView, name='login'),
    path('logout/', views.logoutUser, name='logout'),
]