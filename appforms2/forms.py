from django import forms
morf=(
    ('Male','MALE'),
    ('Female','FEMALE'),
)
citychoice=(
    ('delhi','Delhi'),
    ('damascus','Damascus'),
    ('istambul','Istambul'),
    ('newyork','NewYork'),
    ('london','London'),
    ('berlin','Berlin'),
)
class myform1(forms.Form):
    name=forms.CharField(max_length=20)
    phone=forms.CharField(max_length=15)
    address=forms.CharField(widget=forms.Textarea())
    gender = forms.ChoiceField(widget=forms.RadioSelect, choices=morf)
    city=forms.CharField(widget=forms.Select(choices=citychoice))
    email=forms.EmailField(max_length=20)
    confphone=forms.CharField(max_length=20)
    image=forms.FileField()

class checklog(forms.Form):
    name = forms.CharField(max_length=20)
    phone = forms.CharField(max_length=15)