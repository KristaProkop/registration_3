# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import User #CustomUser
from .forms import MainForm, CreditCardForm #CustomUserForm

#formdict.py contains lookup values for form fields and urls
from .formdict import FORMDICT, URLSDICT


def index(request):
    return render(request, 'register/index.html')


def myView(request, **string_path):
    users = User.objects.all()
    for user in users:
        for item in user:
            print item
    path = request.path

    referer = request.META.get('HTTP_REFERER')
    
    #If path is not in the URLSDICT, use 'default' settings in FORMSDICT
    if path in URLSDICT:
        lookup_path = URLSDICT[path]
    else:
        lookup_path = FORMDICT['default']
    
    #get user fields for form
    user_fields = tuple(lookup_path['user_fields'])
    request.session['user_fields'] = user_fields
    user_form = MainForm(user_fields, request.POST or None)

    #get cc fields for form
    credit_card_fields = tuple(lookup_path['credit_card_fields'])
    request.session['credit_card_fields'] = credit_card_fields
    credit_card_form = CreditCardForm(credit_card_fields, request.POST or None)

    
    if request.method == 'POST':
        if user_form.is_valid() and credit_card_form.is_valid():
                user = User.objects.create_user(username=request.POST['email'], email=request.POST['email'])
              
                # WHY ISNT THIS WORKING???
                for item in request.POST:
                    for field in user_fields:
                        if item == field:
                            print request.POST[field], item
                            item == str(item)
                            user.item = str(request.POST[field])
                            user.save()
                
        

                # user.first_name = 'test'
                # user.save()
                # Did not user form.save() because I am saving email as username
                # user_form.save()
            
            # credit_card_form.save()
            
          

    context = {
        'user_form': user_form,
        'credit_card_form': credit_card_form,
        'heading': lookup_path['heading'],
        'subheading': lookup_path['subheading'],
        'string_path': string_path['string_path'],
    }

    return render(request, 'register/modal.html', context)


# def testing(request):
#     form = CustomUserForm(request.POST)
#     if form.is_valid():
#         form.save()
#     return redirect('/')

# def modal(request, string):
#     path = request.path
    
#     #If path is not in the URLSDICT, use 'default' settings in FORMSDICT
#     if path in URLSDICT:
#         lookup_path = URLSDICT[path]
#     else:
#         lookup_path = FORMDICT['default']
    
#     #get user fields for form
#     user_fields = tuple(lookup_path['user_fields'])
#     request.session['user_fields'] = user_fields
  
#     #get cc fields for form
#     credit_card_fields = tuple(lookup_path['credit_card_fields'])
#     request.session['credit_card_fields'] = credit_card_fields
    
#     #instantiate forms and send to template to combine into one div
#     context = {
#         'user_form': MainForm(user_fields),
#         'credit_card_form': CreditCardForm(credit_card_fields),
#         'heading': lookup_path['heading'],
#         'subheading': lookup_path['subheading'],
#     }
   
#     return render(request, 'register/modal.html', context)

# def register(request):
#     if request.method == "POST":
#         user_fields = request.session['user_fields']
#         credit_card_fields = request.session['credit_card_fields']

#         user_form = MainForm(tuple(user_fields), request.POST)
#         credit_card_form = CreditCardForm(tuple(credit_card_fields), request.POST)


#         if user_form.is_valid():
#             print "saved"
#         else:
#             print "user form problem"
#             return redirect('/')

#         if credit_card_form.is_valid():
#             print "Success credit card!"
#         else:
#             print "something wrong with cc"

#         return redirect('/')

