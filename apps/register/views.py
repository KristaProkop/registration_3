# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth import login

from .models import User
from .forms import MainForm, CreditCardForm

#config.py contains lookup values for form fields and urls
from .config import FORMDICT, URLSDICT


def index(request):
    print request.user
    return render(request, 'register/index.html')


def myView(request, **string_path):
    path = request.path

    #If path is not in the URLSDICT, use 'default' settings in FORMSDICT
    if path in URLSDICT:
        lookup_path = URLSDICT[path]
    else:
        lookup_path = FORMDICT['default']
    
    #get user fields for form.Save fields to session to re-render form properly on input error
    user_fields = tuple(lookup_path['user_fields'])
    request.session['user_fields'] = user_fields
    user_form = MainForm(user_fields, request.POST or None)

    #get cc fields for form
    credit_card_fields = tuple(lookup_path['credit_card_fields'])
    request.session['credit_card_fields'] = credit_card_fields
    credit_card_form = CreditCardForm(credit_card_fields, request.POST or None)

    
    if request.method == 'POST':
        if user_form.is_valid() and credit_card_form.is_valid():
            new_user = user_form.save()
            # only if credit card fields are included on the form, save the cc form
            if len(credit_card_fields) > 0:
                credit_card_form.save(user=new_user)
            login(request, new_user)
            return redirect('/')
            

    context = {
        'user_form': user_form,
        'credit_card_form': credit_card_form,
        'heading': lookup_path['heading'],
        'subheading': lookup_path['subheading'],
        'button_text': lookup_path['button_text'],
        'string_path': string_path['string_path'],

    }

    return render(request, 'register/modal.html', context)

