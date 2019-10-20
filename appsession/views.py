from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from .forms import myform1
from .models import myformsession
# Create your views here.
def login(request):
    form=myform1()
    return render(request,"login.html",{'form':form})
def myform1temp(request):
    if request.method == "POST":
        form = myform1(request.POST,request.FILES)
        if form.is_valid():
            # my1 = myformsession()
            user = form.cleaned_data['user1']
            passw = form.cleaned_data['pass1']
            try:
                current_user=myformsession.objects.get(user1=user,pass1=passw)
                request.session['username']=user
                # return HttpResponse("hellooo")
                print(current_user.user1)
                return render(request,"temper.html")
                # return HttpResponse("hellooo")
            except:
                return redirect('')
    # else:
    #     form = myformsession()
    # return render(request, "login.html", {'form': form})
def viewsession(request):
    user=request.session['username']
    return HttpResponse(user)

def logout(request):
    user = request.session['username']
    print(user)
    if request.session['username']:
        del request.session['username']
    else:
        print("ELSE COND")
    # del request.session['username']
    form = myform1()
    return render(request, "login.html", {'form': form})