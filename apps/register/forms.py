from django import forms

from .models import User, CreditCard


def MainForm(field_list, *args, **kwargs):
    class MainForm(forms.ModelForm):
        if 'password' in field_list:
            password = forms.CharField(widget=forms.PasswordInput())

        class Meta:
            model = User
            fields = field_list

        def __init__(self):
            super(MainForm, self).__init__(*args, **kwargs)

    return MainForm()


def CreditCardForm(field_list, *args, **kwargs):
    class CreditCardForm(forms.ModelForm):
        class Meta:
            model = CreditCard
            fields = field_list

        def __init__(self):
            super(CreditCardForm, self).__init__(*args, **kwargs)
    
    return CreditCardForm() 