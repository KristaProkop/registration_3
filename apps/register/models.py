# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User 


# TODO: Custom date field for expiry? Encrypt CC info before save

class CreditCard(models.Model):
    user = models.ForeignKey(User)
    card_num = models.CharField(max_length=16)
    expiry = models.DateField()
    cvv = models.CharField(max_length=4)

