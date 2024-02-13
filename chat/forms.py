from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'password1', 'password2']
        
        widgets = {
            'username'   : forms.TextInput(attrs= {'class' : 'form-control'}),
            'first_name' : forms.TextInput(attrs = {'class':'form-control'}),
            'last_name'  : forms.TextInput(attrs = {'class':'form-control'}),    
            # 'password1' : forms.PasswordInput(attrs = {'class':'form-control', 'type':'password'}),
            # 'password2' : forms.PasswordInput(attrs = {'class':'form-control', 'type':'password'}),
        }

    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'form-control'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'form-control'})

