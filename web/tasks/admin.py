from django.contrib import admin

from . import models


class TaskAdmin(admin.ModelAdmin):
    list_display = ["pk", "name", "description"]


admin.site.register(models.Task, TaskAdmin)
