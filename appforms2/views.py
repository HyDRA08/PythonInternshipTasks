from django.shortcuts import render
from django.http import HttpResponse
from .forms import myform1,checklog
from .models import myform
# Create your views here.
def home(request):
    form=myform1()                                         # object for myform1 contains the full contents of the form
    return render(request,"form.html",{'form':form})
def myformtemp(request):
    if request.method == "POST":
        form = myform1(request.POST,request.FILES)
        if form.is_valid():                                #check if form is valid?
            contact1 = myform()                            #contact1 is the object for the model myform
            contact1.name = form.cleaned_data['name']      #collecting data
            contact1.phone = form.cleaned_data['phone']    #collecting data
            contact1.address = form.cleaned_data['address']#collecting data
            contact1.gender = form.cleaned_data['gender']  #collecting data
            contact1.city = form.cleaned_data['city']      #collecting data
            contact1.email = form.cleaned_data['email']    #collecting data
            contact1.image = form.cleaned_data['image']    #collecting data
            if contact1.phone == contact1.name:
                contact1.save()
            else:
                return HttpResponse("NOT CORRECT")
                form = myform()
                return render(request, "form.html", {'form': form})
    else:
        form = myform()
        return render(request, "form.html", {'form': form})

def homelog(request):
    formlog=checklog()                                         # object for myform1 contains the full contents of the form
    return render(request,"htmls.html",{'form':formlog})

def check(request):
    if request.method == "POST":
        form = checklog(request.POST,request.FILES)
        if form.is_valid():
            contactcheck = myform()
            nametemp=form.cleaned_data['name']
            phonetemp=form.cleaned_data['phone']



def db(request):
    my = myform.objects.all()
    print(my)
    return render(request, "print.html", {'name_details': my})
