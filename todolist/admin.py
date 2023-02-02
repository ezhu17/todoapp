from django.contrib import admin
from .models import Todolist

# Register your models here.
admin.site.register(Todolist)
#class TodolistAdmin(admin.ModelAdmin):
#    list_display = ('id', 'text', 'completed')