#!/usr/bin/env python3

from django.forms import ModelForm
from django.forms import widgets

from . import models


class BaseForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            widget = visible.field.widget
            match widget.__class__:
                case widgets.RadioSelect:
                    widget.attrs['class'] = 'form-check-input'
                case widgets.CheckboxInput:
                    widget.attrs['class'] = 'form-check-input'
                case _:
                    widget.attrs['class'] = 'form-control'


class AddTaskForm(BaseForm):
    '''Formulario alta de tarea.
    '''

    class Meta:
        '''Configuración del formulario.
        '''
        model = models.Task
        fields = [
            'name',
            'description',
            'urgent',
            ]
        ordered = ('pk',)


class EditTaskForm(BaseForm):
    '''Formulario edición de tarea.
    '''

    class Meta:
        '''Configuración del formulario.
        '''
        model = models.Task
        fields = [
            'name',
            'description',
            'urgent',
            'completed',
            ]
        ordered = ('pk',)
