from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *




class CollegeViewSet(viewsets.ModelViewSet):
    queryset=College.objects.all()
    serializer_class=CollegeSerializers



class StudentViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializers