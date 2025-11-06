#!/usr/bin/env python3

from django.shortcuts import render

from . import models


def homepage(request):
    return render(request, 'tasks/homepage.html', {
        'title': 'OlaKAse - Gestor de tareas',
        'tasks': models.Task.objects.all() 
        })
