from django.contrib import admin
from .models import Beneficiary, Employee, AdminStaff

# Register your models here.

admin.site.register(AdminStaff)
admin.site.register(Beneficiary)
admin.site.register(Employee)