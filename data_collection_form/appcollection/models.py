from django.db import models


# Create your models here.

class Details(models.Model):
    student_name=models.CharField(max_length=100)
    student_age=models.IntegerField(max_length=50)
    
