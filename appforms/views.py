from django.shortcuts import render
from .forms import contactform1
from .models import contactform
# Create your views here.
def contact(request):
    form=contactform1()
    return render(request,"contact.html",{'form':form})
def contacttemp(request):
    if request.method=="POST":
        form=contactform1(request.POST)
        if form.is_valid():
            contact1=contactform()
            contact1.name=form.cleaned_data['name']
            contact1.phone=form.cleaned_data['phone']
            contact1.address=form.cleaned_data['address']
            contact1.save()
    else:
        form1=contactform()
    return render(request,"contact.html",{'form':form})