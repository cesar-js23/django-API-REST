from django.contrib import admin
from .models import *
# Register your models here.

class AlumnoAdmin(admin.ModelAdmin):
    list_display = ('nombre','apellido','telefono','correo','direccion')

class MatriculaAdmin(admin.ModelAdmin):
    list_display = ('codigo','fk_alumno','tipo','fecha','curso','carrera')

admin.site.register(Alumno,AlumnoAdmin)
admin.site.register(Matricula,MatriculaAdmin)