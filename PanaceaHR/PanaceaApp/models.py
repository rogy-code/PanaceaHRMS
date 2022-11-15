from django.db import models

# Create your models here.


class Department(models.Model):
    name = models.CharField(max_length=70, null=False, blank=False)
    history = models.TextField(max_length=1000, null=True, blank=True, default='No History')

    def __str__(self):
        return self.name


class Employee(models.Model):
    GENDER = (('male', 'MALE'), ('female', 'FEMALE'), ('other', 'OTHER'))
    fullname = models.CharField(max_length=255, blank=True, null=True)
    dateofbirth = models.DateField(blank=True, null=True)
    gender = models.CharField(choices=GENDER, max_length=10, blank=True, null=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    position = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    idnumber = models.CharField(max_length=20, blank=True, null=True)
    telephone = models.CharField(max_length=20, blank=True, null=True)
    idphoto = models.ImageField(upload_to='static/media', blank=True, null=True)
    nssfphoto = models.ImageField(upload_to='static/media', blank=True, null=True)
    nhifphoto = models.ImageField(upload_to='static/media', blank=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.fullname[0:50]


class Sallary(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    allowance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    nhif = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    nssf = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    netSalary = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return self.employee.fullname[0:50]

    @property
    def netSalary(self):
        return (self.salary + self.allowance)-(self.nhif + self.nssf)

    @property
    def total_income(self):
        return (self.salary + self.allowance)

    @property
    def total_deductions(self):
        return (self.nhif + self.nssf)
    
    @property
    def expenditure(self):
        return (self.netSalary)
