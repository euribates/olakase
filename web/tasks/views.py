#!/usr/bin/env python3

from django.shortcuts import render, redirect

from . import models
from . import forms

def homepage(request):
    return render(request, 'tasks/homepage.html', {
        'title': 'OlaKAse - Gestor de tareas',
        'tasks': models.Task.objects.all() 
        })


def add_task(request):
    if request.method == 'POST':
        form = forms.AddTaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = forms.AddTaskForm()
    return render(request, 'tasks/add-task.html', {
        'title': 'Añadir tarea',
        'form': form, 
        })
