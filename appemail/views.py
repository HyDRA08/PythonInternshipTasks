from django.shortcuts import render
from django.core.mail import send_mail,EmailMessage
from .forms import mailform
from django.http import HttpResponse
# Create your views here.
def home(request):
    form=mailform()
    if request.method=="POST":
        form = mailform(request.POST)
        if form.is_valid():
            senter=form.cleaned_data['senter']
            recipient_list=[form.cleaned_data['reciver'],]
            subject=form.cleaned_data['subject']
            message=form.cleaned_data['message']
            send_mail(subject,message,senter,recipient_list)
            return HttpResponse("MAIL SENT")
    else:
        # form=mailform()
        return render(request,"mailhome.html",{'form':form})

def email(request):
    form=mailform()
    if request.method == "POST":
        form = mailform(request.POST)
        if form.is_valid():
            senter=form.cleaned_data['senter']
            recipient_list=[form.cleaned_data['reciver'],]
            subject=form.cleaned_data['subject']
            message=form.cleaned_data['message']
            mail=EmailMessage(subject,message,senter,recipient_list)
            mail.send()
            return HttpResponse("MAIL SENT VIA EMAIL MESSAGE")
    else:
        # form=mailform()
        return render(request,"mailhome.html",{'form':form})