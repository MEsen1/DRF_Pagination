from fscohort.models import Student, Course
from .serializers import StudentSerializer, CourseSerializer
from rest_framework import generics
from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

class StudentListCreateAPIView(generics.ListCreateAPIView):
    
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
   
    
class StudentDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_field="id"

class CourseListCreateAPIView(generics.ListCreateAPIView):
    
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
