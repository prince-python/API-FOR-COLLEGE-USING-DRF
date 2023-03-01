from rest_framework import serializers
from . models import *



class CollegeSerializers(serializers.HyperlinkedModelSerializer):
    College_id=serializers.ReadOnlyField()
    class Meta:
        model=College
        fields="__all__"

class StudentSerializers(serializers.HyperlinkedModelSerializer):
    Student_id=serializers.ReadOnlyField()
    class Meta:
        model=Student
        fields="__all__"