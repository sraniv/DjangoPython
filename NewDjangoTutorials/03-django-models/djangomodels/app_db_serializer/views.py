from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from .StudentSerializer import StudentsSerializer
from .models import Students

# Create your views here.
class GetStudent(ListAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer

class GetAllStudents(ListAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer

class InsertStudentData(CreateAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer

class UpdateStudentData(UpdateAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer

class DeleteStudentData(DestroyAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer
