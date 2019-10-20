from django import forms
morf=(
    ('male','male'),
    ('female','female')
)
class contactform1(forms.Form):
    name=forms.CharField(max_length=20)
    phone=forms.CharField(max_length=15)
    address=forms.CharField(widget=forms.Textarea())
    gender = forms.ChoiceField(widget=forms.RadioSelect, choices=morf)
    def clean_name(self):
        name1=self.cleaned_data['name']
        if name1=="":
            print(name1)
            raise forms.ValidationError("errrror")
        return name1