from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from .models import Users, CreditCard #CustomUser

import re

def MainForm(field_list, *args, **kwargs):
    class MainForm(forms.ModelForm):
        if 'password' in field_list:
            password = forms.CharField(widget=forms.PasswordInput())

        class Meta:
            model = Users
            fields = field_list

        def __init__(self):
            super(MainForm, self).__init__(*args, **kwargs)

        def clean(self):
            cleaned_data = self.cleaned_data
            
            #validate email address
            if 'email' in field_list:
                email_regex = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
                email = cleaned_data.get("email")
                if not email_regex.match(email):
                    self.add_error('email', "Invalid email address" )

            #validate names
            if 'first_name' in field_list:
                first_name = cleaned_data.get('first_name')
                if len(first_name) < 2:
                    self.add_error('first_name', "Name must be 2 or more characters" )

            if 'last_name' in field_list:
                last_name = cleaned_data.get('last_name')
                if len(last_name) < 2:
                    self.add_error('last_name', "Name must be 2 or more characters" )
            
            if 'password' in field_list:
                password = cleaned_data.get('password')         
                if len(password) < 8:
                    self.add_error('password', "Password must be 8 or more characters" )

               
            return self.cleaned_data

    return MainForm()


def CreditCardForm(field_list, *args, **kwargs):
    class CreditCardForm(forms.ModelForm):
        class Meta:
            model = CreditCard
            fields = field_list

        def __init__(self):
            super(CreditCardForm, self).__init__(*args, **kwargs)
    
    return CreditCardForm() 

# class CustomUserForm(forms.ModelForm):
#     class Meta:
#         model = CustomUser
#         fields = ['test']