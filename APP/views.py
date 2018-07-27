# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import JsonResponse
from django.shortcuts import render


def hello(request):
    data = {
        'msg': 'hello bbs'
    }
    return JsonResponse(data)
