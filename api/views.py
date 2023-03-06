from rest_framework import generics, permissions, status
from django.db import IntegrityError
from django.contrib.auth.models import User
from rest_framework.parsers import JSONParser
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse, QueryDict, Http404
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
from .serializers import EmployeeSerializer, BeneficiatySerializer, CreateEmployeeSerializer
from employee.models import Employee, Beneficiary
from rest_framework.parsers import MultiPartParser, FormParser
import json
from drf_excel.mixins import XLSXFileMixin
from drf_excel.renderers import XLSXRenderer
from rest_framework.viewsets import ReadOnlyModelViewSet


# Create your views here.

class EmployeesList(generics.ListAPIView):
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticated]

    queryset = Employee.objects.all().order_by('-created')


class BeneficiaryList(generics.ListAPIView):
    serializer_class = BeneficiatySerializer
    permission_classes = [permissions.IsAuthenticated]

    queryset = Beneficiary.objects.all()


class CreateEmployeeView(APIView):
    serializer_class = CreateEmployeeSerializer
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, format=None):
        query_dict = QueryDict('', mutable=True)
        new_beneficiary = json.loads(request.data['beneficiary'])
        query_dict.update(new_beneficiary)
        n_ben = BeneficiatySerializer(data=query_dict)


        if n_ben.is_valid():
            benficiary = n_ben.save()

        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()

        new_form = {
            "name": request.data.get('name'),
            "position": request.data.get('position'),
            "salary": request.data.get('salary'),
            "_status": request.data.get('status'),
            "date_of_hire": request.data.get('date_of_hire'),
            "beneficiary": benficiary.id,
            "email": request.data.get('email'),
            "photo": request.data.get('photo'),
        }
        serializer = self.serializer_class(data=new_form)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # def put(self, request, id, format=None):
    #     employee = Employee.objects.get(pk=id)
    #     new_form = {
    #         "name": request.data.get('name'),
    #         "position": request.data.get('position'),
    #         "salary": request.data.get('salary'),
    #         "status": request.data.get('status'),
    #         "date_of_hire": request.data.get('date_of_hire'),
    #         "beneficiary": request.data.get('beneficiary'),
    #         "email": request.data.get('email'),
    #         "photo": request.data.get('photo'),
    #     }

    #     serializer = EmployeeSerializer(employee, data=new_form)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_200_OK)
        
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EmployeeDetails(generics.RetrieveAPIView):
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        return Employee.objects.all()


class EmployeesCreateList(generics.ListCreateAPIView):
    serializer_class = CreateEmployeeSerializer
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = (MultiPartParser, FormParser)

    def get_queryset(self):
        return Employee.objects.all().order_by('-created')
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class DeleteEmployeeView(APIView):
    serializer_class = EmployeeSerializer

    def get_object(self, pk):
        try:
            return Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            raise Http404

    def delete(self, request, pk, format=None):
        employee = self.get_object(pk)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class EmployeeRetriveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user_id = self.request.data['id']
        return Employee.objects.filter(id=user_id)

class ExportData(XLSXFileMixin, ReadOnlyModelViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    renderer_classes = [XLSXRenderer]
    filename = 'employees.xlsx'
    

@csrf_exempt
def signup(request):
    if request.method == 'POST':
        try:
            data = JSONParser().parse(request)
            user = User.objects.create_user(
                username=data['username'],
                password=data['password'],
            )

            user.save()
            token = Token.objects.create(user=user)

            return JsonResponse({ 'token': str(token) }, status=201)
        except IntegrityError:
            return JsonResponse({ 'error': 'Username taken. Choose another.' }, status=400)


@csrf_exempt
def login(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        user = authenticate(
            request,
            username = data['username'],
            password = data['password'],
        )
        if user is None:
            return JsonResponse(
                { 'Error': 'Unable to login. Username and password are incorrect' },
                status=400
            )
        else:
            try: # Return a user token
                token = Token.objects.get(user=user)
            except:# If not exist, create a new one
                token = Token.objects.create(user=user)

            return JsonResponse(
                { 'token': str(token) },
                status=201
            )
