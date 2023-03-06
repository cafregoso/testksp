from django.urls import path
from . import views

urlpatterns = [
    path('employees/', views.EmployeesList.as_view()),
    path('employees/create/', views.CreateEmployeeView.as_view()),
    path('employee/<str:pk>', views.EmployeeDetails.as_view()),
    path('employee/delete/<str:pk>', views.DeleteEmployeeView.as_view()),
    path('beneficiaries/', views.BeneficiaryList.as_view()),
    path('signup/', views.signup),
    path('login/', views.login),
    path('download/', views.ExportData.as_view({'get': 'list'}), name='Descargar registro'),
]