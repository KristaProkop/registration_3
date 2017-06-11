# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models



# Create your models here.
class CCManager(models.Manager):

    def validate_email(request, postData):
        email_regex = "regex"
        #validate email
        #return request object or raise error
        return True


class Users(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.CharField(max_length=75, blank=False, unique=True)
    password = models.CharField(max_length=100)


class CreditCard(models.Model):
    user = models.ForeignKey(Users)
    card_num = models.CharField(max_length=16)
    expiry = models.DateField()
    cvv = models.CharField(max_length=4)
    objects = CCManager()

