from django.shortcuts import render
from rest_framework import viewsets

from .serializer import StudentSerializer
from student.models import Student

from .serializer import TeacherSerializer
from teacher.models import Teacher

from .serializer import CourseSerializer
from Course.models import Course

class StudentViewSet(viewsets.ModelViewSet):
	queryset = Student.objects.all()
	serializer_class = StudentSerializer
	
class TeacherViewSet(viewsets.ModelViewSet):
	queryset = Teacher.objects.all()
	serializer_class = TeacherSerializer

class CourseViewSet(viewsets.ModelViewSet):
	queryset = Course.objects.all()
	serializer_class = CourseSerializer	
	
# Create your views here.
