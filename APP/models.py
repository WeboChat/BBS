# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class UserModel(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=16,unique=True)
    password = models.CharField(max_length=128)
    icon = models.ImageField(upload_to='icons')
    sex = models.CharField(max_length=16)

    class Meta:
        db_table = '用户表'

class TieZi(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=128)
    user = models.CharField(max_length=128)
    content = models.TextField(max_length=256)

    class Meta:
        db_table = '帖子表'


