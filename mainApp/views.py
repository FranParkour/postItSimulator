from django.shortcuts import render, redirect
from .models import Tarea

def index(request):
    tareas = Tarea.objects.all()
    data = {'tareas': tareas}
    return render(request, 'index.html', data)

def agregarTarea(request):
    titulo = request.POST['titulo']
    descripcion = request.POST['descripcion']
    importante = request.POST.get('importante') == 'on'

    tarea = Tarea.objects.create(titulo=titulo, descripcion=descripcion, importante=importante)
    return redirect('/')

def eliminarTarea(request, id):
    tarea = Tarea.objects.get(id=id)
    tarea.delete()
    return redirect('/')