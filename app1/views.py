from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# def new(request):
    # return HttpResponse("APP-1")
def temp(request):
    # print("HELOOOOOOO")
    # return HttpResponse("NEXT WINDOWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW")
    # text="HEllowwowowow WOLRDDDDDDD"
    return render(request,"layout.html")
def temp1(request):
    return render(request,"layout1.html")
def temp2(request):
    return render(request,"layout2.html")
def temp3(request):
    return render(request,"layout3.html")