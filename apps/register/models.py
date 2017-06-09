# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class CCManager(models.Manager):
    def test(request):
        return True
        

class CreditCard(models.Model):
    user = models.ForeignKey(User)
    card_num = models.CharField(max_length=16)
    expiry = models.DateField()
    cvv = models.CharField(max_length=4)
    objects = CCManager()