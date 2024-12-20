from django.db import models

class Tarea(models.Model):
    titulo = models.CharField(max_length=50)
    descripcion = models.TextField()
    importante = models.BooleanField(default=False)