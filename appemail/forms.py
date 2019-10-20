from django import forms

class mailform(forms.Form):
    senter=forms.CharField(max_length=50)
    reciver=forms.CharField(max_length=50)
    subject=forms.CharField(max_length=50)
    message=forms.CharField(max_length=50)

