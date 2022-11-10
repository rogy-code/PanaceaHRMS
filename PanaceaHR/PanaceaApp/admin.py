from django.contrib import admin
from . models import Employee,Sallary,Department

# Register your models here.
admin.site.register(Employee)
admin.site.register(Sallary)
admin.site.register(Department)