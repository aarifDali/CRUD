from django import forms
from adpanel.models import  UserProfile
from django.core import validators

class UserRegistration(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['username', 'first_name', 'last_name']
        widgets = {
            'username' : forms.TextInput(attrs={'class' : 'form-control col-3'}),
            'first_name' : forms.TextInput(attrs={'class' : 'form-control col-3'}),
            'last_name' : forms.TextInput(attrs={'class' : 'form-control col-3'}),
           
        }
        