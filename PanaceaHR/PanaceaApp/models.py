from django.db import models

# Create your models here.

class Employee(models.Model):
    fullname = models.CharField(max_length=255, blank=True, null=True)
    dateofbirth = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=20, blank=True, null=True)
    idnumber = models.CharField(max_length=20, blank=True, null=True)
    telephone = models.CharField(max_length=20, blank=True, null=True)
    idphoto = models.ImageField(upload_to='media', blank=True, null=True)
    nssfphoto = models.ImageField(upload_to='media', blank=True, null=True)
    nhifphoto = models.ImageField(upload_to='media', blank=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.fullname[0:50]
