#!/usr/bin/env python3

from django.shortcuts import render, redirect

from . import models
from . import forms


def homepage(request):
    """Página de inicio (*Homepage*).
    """
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


def view_task(request, id_task: int):
    task = models.Task.load_task(id_task)
    return render(request, 'tasks/view-task.html', {
        'title': task.name,
        'task': task,
        })


def edit_task(request, id_task: int):
    task = models.Task.load_task(id_task)
    if request.method == 'POST':
        form = forms.EditTaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = forms.EditTaskForm(instance=task)
    return render(request, 'tasks/edit-task.html', {
        'title': f'Modificar valores para la tarea {task.pk}',
        'subtitle': task.name,
        'task': task,
        'form': form,
        })
