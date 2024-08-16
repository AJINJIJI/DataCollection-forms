from django.shortcuts import render
from appcollection.models import Details
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request,"index.html")

def data(request):
    student_name=request.POST['a']
    student_age=request.POST['b']
    student_marks=request.POST['c']
    subject=request.POST['d']
    data=Details(student_name=student_name,student_age=student_age)
    data.save()
    
    
    if int(student_age) >=18 and int(student_marks) >=40:
        return render (request,"index.html",{"content1":"Eligible"})
   
    elif int(student_age) <=18 and int(student_marks) <=40 :
        return render (request,"index.html",{"content2":" Not Eligible"})