# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import User
from .forms import MainForm, CreditCardForm

#formdict.py contains lookup values for form fields and urls
from .formdict import FORMDICT, URLSDICT


def index(request):
    return render(request, 'register/index.html')


def modal(request, string):
    path = request.path
    
    #If path is not in the URLSDICT, use 'default' settings in FORMSDICT
    if path in URLSDICT:
        lookup_path = URLSDICT[path]
    else:
        lookup_path = FORMDICT['default']

    #instantiate user form with corresponding fields
    user_fields = tuple(lookup_path['user_fields'])
    request.session['user_fields'] = user_fields
  
    #instantiate credit card form with corresponding fields
    credit_card_fields = tuple(lookup_path['credit_card_fields'])
    request.session['credit_card_fields'] = credit_card_fields
    
    #pass both forms to template & combine into one form div
    context = {
        'user_form': MainForm(user_fields),
        'credit_card_form': CreditCardForm(credit_card_fields),
        'heading': lookup_path['heading'],
        'subheading': lookup_path['subheading'],
    }
   
    return render(request, 'register/modal.html', context)

def register(request):
    if request.method == "POST":
        user_fields = request.session['user_fields']
        credit_card_fields = request.session['credit_card_fields']

        user_form = MainForm(tuple(user_fields), request.POST)

        if user_form.is_valid():
            print "Success user!"
        else:
            print "user form problem"

        credit_card_form = CreditCardForm(tuple(credit_card_fields), request.POST)

        if credit_card_form.is_valid():
            print "Success credit card!"
        else:
            print "something wrong with cc"

        return redirect('/')



