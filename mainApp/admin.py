from django.contrib import admin
from .models import Tarea

class TareaAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'descripcion']

admin.site.register(Tarea, TareaAdmin)