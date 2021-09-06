from django.db import models

# Create your models here.

class Alumno(models.Model):
    nombre = models.CharField(max_length=45,blank=False)
    apellido = models.CharField(max_length=45, blank=False)
    telefono = models.IntegerField(blank=False)
    correo = models.EmailField(blank=False)
    direccion = models.CharField(max_length=100,blank=False)

    def __str__(self):
        return self.nombre


tipo_matricula = [
    ('ORDINARIA','ORDINARIA'),
    ('EXTRAORDINARIA', 'EXTRAORDINARIA'),
    ('ESPECIAL', 'ESPECIAL'),
]

tipo_curso = [
    ('1','I CICLO'),
    ('2','II CICLO'),
    ('3','III CICLO'),
    ('4','IV CICLO'),
    ('5','V CICLO'),
]

class Matricula(models.Model):
    codigo = models.CharField(max_length=8,blank=False)
    tipo = models.CharField(max_length=45,choices=tipo_matricula,default='available')
    fecha = models.DateField(blank=False)
    curso = models.CharField(max_length=45,choices=tipo_curso,default='available')
    carrera = models.CharField(max_length=100,blank=False)
    fk_alumno = models.OneToOneField(Alumno,on_delete=models.CASCADE,blank=False)

    def __str__(self):
        return self.tipo




























