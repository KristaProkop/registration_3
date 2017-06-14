from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


from .models import User, CreditCard 

import re
from datetime import datetime



def MainForm(field_list, *args, **kwargs):
    class MainForm(forms.ModelForm):
        # password fields must be password widgets
        if 'password' in field_list:
            password = forms.CharField(label="Password", widget=forms.PasswordInput())

        class Meta:
            model = User
            fields = field_list

        def clean_first_name(self):
            # names must be 2 or more chars with no digits
            self.cleaned_data['first_name'] = self.cleaned_data['first_name'].title()

            first_name = self.cleaned_data['first_name']
            if len(first_name) < 2:
                self.add_error('first_name', "Name must be 2 or more characters" )
            if any(char.isdigit() for char in first_name):
                self.add_error('first_name', 'Name cannot contain numbers')
            return first_name

        def clean_last_name(self):
            self.cleaned_data['last_name'] = self.cleaned_data['last_name'].title()
            last_name = self.cleaned_data['last_name']

            if len(last_name) < 2:
                self.add_error('last_name', "Name must be 2 or more characters" )
            if any(char.isdigit() for char in last_name):
                self.add_error('last_name', 'Name cannot contain numbers')
            return last_name

        def clean_email(self):
             # Django email field already validates email pattern

                        # email_regex = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")

                        # email = cleaned_data['email']

                        # if not email_regex.match(email):
                        #     self.add_error('email', "Invalid email address" )
            email = self.cleaned_data['email']
            try:
                user = User.objects.get(username=email)
                self.add_error('email', "Account already exists! Please log in instead")
            except: 
                return email

        def clean_password(self):
            # password must be 8 or more char with one letter and one number
            password = self.cleaned_data['password']
            
            if len(password) < 8 or not (any(char.isdigit() for char in password)) or not (any(char.isalpha() for char in password)):
                self.add_error('password', "Password must be 8 or more characters and must contain at least 1 letter and 1 number" )

            # if form contains "confirm password field", check for match with password
            if 'conf_password' in self.cleaned_data:
                conf_password = self.cleaned_data['conf_password']
                if password != conf_password:
                    self.add_error('password', "Passwords must match")
            return password


        # override save function to assign email as username, as username is required for django authentication
        def save(self, commit=True):
            user = super(MainForm, self).save(commit=False)
            user.email = self.cleaned_data["email"]
            user.username = user.email
            if commit:
                user.save()
            return user


        def __init__(self):
            super(MainForm, self).__init__(*args, **kwargs)
            for field in self.fields:
                self.fields[field].widget.attrs['placeholder'] = self.fields[field].label   
                self.fields[field].label = False

                # TODO: Pass argument for custom class field 
                # self.fields[field].widget.attrs['class'] = 'my_class'

    return MainForm()


def CreditCardForm(field_list, *args, **kwargs):
    class CreditCardForm(forms.ModelForm):
        class Meta:
            model = CreditCard
            fields = field_list

        def clean(self):
            cleaned_data = self.cleaned_data

            # if card is required, validate card number length and expiration date.
            # TODO: implement Luhn algo to validate numbers and card providers

            if 'card_num' in field_list:
                card_num = cleaned_data.get("card_num")
                expiry = cleaned_data.get("expiry")

                if not len(card_num) == 15:
                    self.add_error('card_num', "Enter a valid Amex number")

                if not expiry > datetime.today().date():
                    self.add_error('expiry', "Enter a valid expiration date")
               
            return self.cleaned_data

        def save(self, user, commit=True):
            # override save function to attach user to credit card record
            credit_card = super(CreditCardForm, self).save(commit=False)
            credit_card.user = user
            if commit:
                credit_card.save()
            return credit_card

  
        def __init__(self):
            super(CreditCardForm, self).__init__(*args, **kwargs)
            # Remove form label and add placeholder for each field
            for field in self.fields:
                self.fields[field].widget.attrs['placeholder'] = self.fields[field].label   
                self.fields[field].label = False



    return CreditCardForm() 

