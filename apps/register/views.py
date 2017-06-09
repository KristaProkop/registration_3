# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import User
from .forms import MainForm

#formdict.py contains lookup values for form fields and urls
from .formdict import FORMDICT, FIELDS, URLSDICT


def index(request):
    return render(request, 'register/index.html')


def modal(request, string):
    path = request.path
    
    if path in URLSDICT:
        lookup_path = URLSDICT[path]
    else:
        lookup_path = FORMDICT['default']

    fields = lookup_path['fields']
    form = MainForm(fields)
    
    context = {
        'form': form,
        'heading': lookup_path['heading'],
        'subheading': lookup_path['subheading'],
    }
   
    return render(request, 'register/modal.html', context)

def register(request):
    if request.method == "POST":
        print request.POST
        path = request.path
        referer = request.META.get('HTTP_REFERER')
        return redirect(referer, kwargs={path})





# def main(request, string):
#     path = request.path
#     forms = {}
#     # Create MainForm for each modal page specified in formdict
#     for page, vals in URLS[path]['pages'].iteritems():
#         forms[page] = MainForm()
     

#     # For each form remove FIELDS that are not specified for this path in formdict
#     for field in forms[page].fields:
#         for page, vals in URLS[path]['pages'].iteritems():
#             if field not in vals:
#                 del forms[page].fields[field]
        
#     heading = URLS[path]['heading']
#     subheading = URLS[path]['subheading']

#     context = {
#         'form': forms[0],
#         'heading': heading,
#         'subheading': subheading,
#     }

#     return render(request, 'register/modal.html', context)
