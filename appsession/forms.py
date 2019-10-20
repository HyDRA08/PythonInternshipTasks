from django import forms

class myform1(forms.Form):
    user1=forms.CharField(max_length=20)
    pass1=forms.CharField(max_length=20)