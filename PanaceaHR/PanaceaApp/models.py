from django.db import models
import decimal

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
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    allowance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    nhif = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    nssf = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    netSalary = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    updated = models.DateTimeField(auto_now=True, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.employee.fullname[0:50]

    @property
    def total_income(self):
        return (self.salary + self.allowance)
    
    # @property
    # def expenditure(self):
    #     return (self.netSalary)
    
    @property
    def nhif(self):
        if (self.salary + self.allowance) >= 0 and (self.salary + self.allowance) <= 5999:
            return(150)
        elif (self.salary + self.allowance) >= 6000 and (self.salary + self.allowance) <=7999:
            return(300)
        elif (self.salary + self.allowance) >= 8000 and (self.salary + self.allowance) <=11999:
            return(400)
        elif (self.salary + self.allowance) >= 12000 and (self.salary + self.allowance) <=14999:
            return(500)
        elif (self.salary + self.allowance) >= 15000 and (self.salary + self.allowance) <=19999:
            return(600)
        elif (self.salary + self.allowance) >= 20000 and (self.salary + self.allowance) <=24999:
            return(750)
        elif (self.salary + self.allowance) >= 25000 and (self.salary + self.allowance) <=29999:
            return(850)
        elif (self.salary + self.allowance) >= 30000 and (self.salary + self.allowance) <=34999:
            return(900)
        elif (self.salary + self.allowance) >= 35000 and (self.salary + self.allowance) <=39000:
            return(950)
        elif (self.salary + self.allowance) >= 40000 and (self.salary + self.allowance) <=44999:
            return(1000)
        elif (self.salary + self.allowance) >= 45000 and (self.salary + self.allowance) <=49000:
            return(1100)
        elif (self.salary + self.allowance) >= 50000 and (self.salary + self.allowance) <=59999:
            return(1200)
        elif (self.salary + self.allowance) >= 60000 and (self.salary + self.allowance) <=69999:
            return(1300)
        elif (self.salary + self.allowance) >= 70000 and (self.salary + self.allowance) <=79999:
            return(1400)
        elif (self.salary + self.allowance) >= 80000 and (self.salary + self.allowance) <=89999:
            return(1500)
        elif (self.salary + self.allowance) >= 90000 and (self.salary + self.allowance) <=99999:
            return(1600)
        else:
            return(1700)

    @property
    def nssf(self):
        if (self.salary + self.allowance) >= 0 and (self.salary + self.allowance) <= 6000:
            return ((self.salary + self.allowance) * (decimal.Decimal(0.06)))
        elif (self.salary + self.allowance) >= 6001 and (self.salary + self.allowance) <=18000:
            return (((self.salary + self.allowance)-6000) * (decimal.Decimal(0.06 )) + 360)    
        else:
            return (1080)
    
    @property
    def paye(self):
        if(self.total_income - self.nssf) >= 0 and (self.total_income - self.nssf) <= 24000:
            return (((self.total_income - self.nssf)* (decimal.Decimal(0.1)))-2400)
        elif (self.total_income - self.nssf) >= 24001 and (self.total_income - self.nssf) <= 32332:
            return ((((self.total_income - self.nssf)-24000) * (decimal.Decimal(0.25 ))))
        else:
            return(((self.total_income - self.nssf)-32332) * (decimal.Decimal(0.3))+ (decimal.Decimal(2083.25)))
    
    @property
    def total_deductions(self):
        return (self.nhif + self.nssf)
    
    @property
    def netSalary(self):
        return (self.total_income)-(self.total_deductions)
    
    @property
    def netPaye(self):
        if self.paye <= 0:
            return(self.netSalary)
        else:
            return(self.netSalary - self.paye)