from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from uuid import uuid4

# Create your models here.

class Beneficiary(models.Model):
    name = models.CharField(max_length=100, verbose_name='Beneficiary Name')
    birthdate = models.DateField(verbose_name='Birhtdate')
    gender = models.CharField(max_length=7, verbose_name='Gender')
    relationship = models.CharField(max_length=25, verbose_name='Relationship')

    def __str__(self) -> str:
        return self.name

class Employee(models.Model):
    id = models.CharField(max_length=60, primary_key=True ,default=str(uuid4()), verbose_name='id')
    name = models.CharField(max_length=200, verbose_name='Complete name')
    email = models.EmailField(unique=True, default=None, verbose_name='Email')
    position = models.CharField(max_length=50)
    salary = models.FloatField(verbose_name='Salary')
    status = models.BooleanField(default=True)
    date_of_hire = models.DateField(verbose_name='Date of Hire')
    photo = models.ImageField(blank=True, upload_to='images', verbose_name='Photo')
    beneficiary = models.ForeignKey(
        Beneficiary,
        on_delete=CASCADE
    )
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name
    
class AdminStaff(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=CASCADE
    )