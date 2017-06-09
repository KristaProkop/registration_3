from django import forms

from .models import User, CreditCard


def MainForm(field_list, *args, **kwargs):
    class MainForm(forms.ModelForm):
        class Meta:
            model = User
            fields = field_list

        def __init__(self):
            super(MainForm, self).__init__(*args, **kwargs)
    
    return MainForm()
