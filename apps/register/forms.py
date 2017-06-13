from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


from .models import User, CreditCard #CustomUser

import re
from datetime import datetime



def MainForm(field_list, *args, **kwargs):
    class MainForm(forms.ModelForm):
        if 'password' in field_list:
            password = forms.CharField(widget=forms.PasswordInput())

        class Meta:
            model = User
            fields = field_list

        def clean(self):
            cleaned_data = self.cleaned_data

            #validate email address
            # if 'email' in field_list:
            #     email_regex = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

            #     email = str(self.fields['email'])

            #     if not email_regex.match(email):
            #         self.add_error('email', "Invalid email address" )

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


        def save(self, commit=True):
            user = super(MainForm, self).save(commit=False)
            user.email = self.cleaned_data["email"]
             # write email to username
            user.username = user.email
            if commit:
                user.save()
            return user

        def __init__(self):
            super(MainForm, self).__init__(*args, **kwargs)


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
            credit_card = super(CreditCardForm, self).save(commit=False)
            credit_card.user = user
            if commit:
                credit_card.save()
            return credit_card

  
        def __init__(self):
            super(CreditCardForm, self).__init__(*args, **kwargs)

    return CreditCardForm() 

