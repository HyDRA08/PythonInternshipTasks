from django.shortcuts import render
from django.http import HttpResponse
from .models import shoping
# Create your views here.
def home(request):
    # print("Home Page")
    shop=shoping.objects.filter(catparentid=0)
    return render(request,"home.html",{'shop':shop})
def sub1(request,id):
    shop = shoping.objects.filter(catparentid=0)
    shop1=shoping.objects.filter(catparentid=id)
    return render(request,"opt1.html",{'shop1': shop1,'shop':shop})
def sub2(request,id):
    shop = shoping.objects.filter(catparentid=0)
    shop1 = shoping.objects.filter(catparentid=id)
    return render(request, "opt2.html", {'shop1': shop1, 'shop': shop})
