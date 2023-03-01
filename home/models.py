from django.db import models



class College(models.Model):
    name=models.CharField(max_length=100)
    location=models.CharField(max_length=200)
    
    addeddate=models.DateField(auto_now=True)
    about=models.TextField()
    active=models.BooleanField(default=True)
    def __str__(self):
        return self.name
    
    
    
class Student(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField()
    college=models.ForeignKey(College, on_delete=models.CASCADE)
    course=models.CharField(max_length=200,choices=(
        ('ENGINEERING','ENGINEERING'), ('BSC','BSC'),('BCOM','BCOM'),('BBA','BBA'),('LAW','LAW')
    ))
    mobile=models.IntegerField()
    def __str__(self):
        return self.name
    

