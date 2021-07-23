from django.contrib import admin
from .models import Todolist


class TodolistAdmin(admin.ModelAdmin):
    fields = ['status', 'priority', 'duedate', 'description', 'name']

admin.site.register(Todolist, TodolistAdmin)
