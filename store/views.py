# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def index(request):
    return render(request, 'template.html') 

def store(request):
    return render(request, 'store.html')
