from django.shortcuts import render
from django.http import HttpResponse
from .models import student
# Create your views here.
def temp11(request):
    return render(request,"orkut.html")
def temp12(request):
    return render(request,"english.html")
def temp23(request):
    return render(request,"french.html")
def temp34(request):
    return render(request,"espanol.html")
def temp45(request):
    return render(request,"turkey.html")
def temp56(request):
    return render(request,"portugeese.html")

def display(request):
    stud=student.objects.all()
    return render(request,"display.html",{'stud1':stud})
def details(request,id):
    st=student.objects.get(FirstName='Shijo',id=id)
    return render(request,"details.html",{'stud_details':st})
