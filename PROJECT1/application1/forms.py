from django import forms
from application1.models import MyModel

class MyForm(forms.ModelForm):
    name = forms.CharField(error_messages={'required':'Please enter your name'})


    class Meta:
        model = MyModel
        fields = ('name',)
