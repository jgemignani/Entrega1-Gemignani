from django import http
from django.shortcuts import render
from .models import Curso, Estudiante, Profesor, Entregable
from django.http import HttpResponse
from AppCoder.forms import CursoFormulario, ProfeFormulario, EstudianteFormulario
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.

def curso(self):
    curso=Curso(nombre="Curso de Django", comision=12345)
    curso.save()
    texto= f"Curso: {curso.nombre} comision: {curso.comision}"
    return HttpResponse(texto)

    
def inicio(request):
    return render(request, 'AppCoder/inicio.html')


def profesores(request):
    return render(request, 'AppCoder/profesores.html')


def estudiantes(request):
    return render(request, 'AppCoder/estudiantes.html')


def entregables(request):
    return render(request, 'AppCoder/entregables.html')

###CURSOS###
def cursos(request):

    if request.method == 'POST':

        miFormulario=CursoFormulario(request.POST)

        if miFormulario.is_valid():
            informacion=miFormulario.cleaned_data
            curso=Curso(nombre=informacion['nombre'], comision=informacion['comision'])
            curso.save()
            return render(request, 'AppCoder/inicio.html')

    else:
        miFormulario=CursoFormulario()
    return render(request, 'AppCoder/cursos.html', {'formulario':miFormulario})

def leerCursos(request):
    cursos=Curso.objects.all()
    contexto={'cursos':cursos}
    
    return render(request, 'AppCoder/leecursos.html', contexto)

def eliminarCurso(request, nombre):
    curso=Curso.objects.get(nombre=nombre)
    curso.delete()

    cursos=Curso.objects.all()
    contexto={'cursos':cursos}
        
    return render(request, 'AppCoder/leecursos.html', contexto)

def editarCurso(request, nombre):
    curso=Curso.objects.get(nombre=nombre)
    if request.method == 'POST':
        formulario=CursoFormulario(request.POST)
        if formulario.is_valid():
            informacion=formulario.cleaned_data
            curso.nombre=informacion['nombre']
            curso.comision=informacion['comision']
            curso.save()
            #Muestro la lista de cursos de nuevo
            cursos=Curso.objects.all()
            contexto={'cursos':cursos}
        
            return render(request, 'AppCoder/cursos.html', contexto)
    else:
        formulario=CursoFormulario(initial={'nombre':curso.nombre, 'comision':curso.comision})
    return render(request, 'AppCoder/editarCurso.html', {'formulario':formulario, 'nombre':nombre})


###CURSOS###

def busquedaComision(request):
    return render(request, 'AppCoder/busquedaComision.html')


def buscar(request):
    if request.GET['comision']:
        comision=request.GET['comision']
        cursos=Curso.objects.filter(comision=comision)
        return render(request, 'AppCoder/resultadosBusqueda.html', {'cursos':cursos, 'comision':comision})
    else:
        respuesta="No se ingreso ninguna comision"
        return render(request, 'AppCoder/resultadosBusqueda.html', {'respuesta':respuesta})

    return render(request, 'AppCoder/cursosFormulario.html')

##PROFESORES###

def leerProfesores(request):
    profesores=Profesor.objects.all()
    contexto={'profesores':profesores}
    
    return render(request, 'AppCoder/profesores.html', contexto)

def eliminarProfesor(request, nombre):
    profesor=Profesor.objects.get(nombre=nombre)
    profesor.delete()

    profesores=Profesor.objects.all()
    contexto={'profesores':profesores}
        
    return render(request, 'AppCoder/profesores.html', contexto)

def editarProfesor(request, nombre):
    profesor=Profesor.objects.get(nombre=nombre)
    if request.method == 'POST':
        formulario=ProfeFormulario(request.POST)
        if formulario.is_valid():
            informacion=formulario.cleaned_data
            profesor.nombre=informacion['nombre']
            profesor.apellido=informacion['apellido']
            profesor.email=informacion['email']
            profesor.profesion=informacion['profesion']
            profesor.save()
            #luego muestro la lista de profes de nuevo
            profesores=Profesor.objects.all()
            contexto={'profesores':profesores}
        
            return render(request, 'AppCoder/profesores.html', contexto)
    else:
        formulario=ProfeFormulario(initial={'nombre':profesor.nombre, 'apellido':profesor.apellido, 'email':profesor.email, 'profesion':profesor.profesion})
    return render(request, 'AppCoder/editarProfesor.html', {'formulario':formulario, 'nombre':nombre})

def agregaProfesor(request):

    if request.method == 'POST':

        miFormulario=ProfeFormulario(request.POST)

        if miFormulario.is_valid():
            informacion=miFormulario.cleaned_data
            profesor=Profesor(nombre=informacion['nombre'], apellido=informacion['apellido'],email=informacion['email'],profesion=informacion['profesion'])
            profesor.save()
            return render(request, 'AppCoder/inicio.html')

    else:
        miFormulario=ProfeFormulario()
    return render(request, 'AppCoder/agregaProfesor.html', {'formulario':miFormulario})

###PROFESORES###

###ESTUDIANTES###

def leerEstudiantes(request):
    estudiantes=Estudiante.objects.all()
    contexto={'estudiantes':estudiantes}
    
    return render(request, 'AppCoder/estudiantes.html', contexto)

def eliminarEstudiante(request, nombre):
    estudiante=Estudiante.objects.get(nombre=nombre)
    estudiante.delete()

    estudiantes=Estudiante.objects.all()
    contexto={'estudiantes':estudiantes}
        
    return render(request, 'AppCoder/estudiantes.html', contexto)

def editarEstudiante(request, nombre):
    estudiante=Estudiante.objects.get(nombre=nombre)
    if request.method == 'POST':
        formulario=EstudianteFormulario(request.POST)
        if formulario.is_valid():
            informacion=formulario.cleaned_data
            estudiante.nombre=informacion['nombre']
            estudiante.apellido=informacion['apellido']
            estudiante.email=informacion['email']
            estudiante.save()
            #luego muestro la lista de estudiantes de nuevo
            estudiantes=Estudiante.objects.all()
            contexto={'estudiantes':estudiantes}
        
            return render(request, 'AppCoder/estudiantes.html', contexto)
    else:
        formulario=EstudianteFormulario(initial={'nombre':estudiante.nombre, 'apellido':estudiante.apellido, 'email':estudiante.email})
    return render(request, 'AppCoder/editarEstudiante.html', {'formulario':formulario, 'nombre':nombre})

def agregaEstudiante(request):

    if request.method == 'POST':

        miFormulario=EstudianteFormulario(request.POST)

        if miFormulario.is_valid():
            informacion=miFormulario.cleaned_data
            estudiante=Estudiante(nombre=informacion['nombre'], apellido=informacion['apellido'], email=informacion['email'])
            estudiante.save()
            return render(request, 'AppCoder/inicio.html')

    else:
        miFormulario=EstudianteFormulario()
    return render(request, 'AppCoder/agregaEstudiante.html', {'formulario':miFormulario})

###ESTUDIANTES###


class EstudiantesList(ListView):
    model = Estudiante
    template_name = 'AppCoder/estudiantes.html'

class EstudianteDetalle(DetailView):
    model = Estudiante
    template_name = 'AppCoder/estudiante_detalle.html'

class EstudianteCreacion(CreateView):
    model = Estudiante
    success_url = reverse_lazy('estudiante_listar')#
    fields=['nombre', 'apellido', 'email']

class EstudianteEdicion(UpdateView):
    model = Estudiante
    success_url = reverse_lazy('estudiante_listar')#
    fields=['nombre', 'apellido', 'email']

class EstudianteEliminacion(DeleteView):
    model = Estudiante
    success_url = reverse_lazy('estudiante_listar')#
    fields=['nombre', 'apellido', 'email']



    








