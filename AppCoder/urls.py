from django.urls import path
from .views import *


urlpatterns = [
    path('', inicio, name='inicio'),
    
   # path('creaCurso', curso),
    
    path('cursos/', cursos, name='cursos'),
    path('agregaProfesor', agregaProfesor, name='agregaProfesor'),
    path('agregaEstudiante', agregaEstudiante, name='agregaEstudiante'),
    path('profesores/', leerProfesores, name='profesores'),
    path('estudiantes/', leerEstudiantes, name='estudiantes'),
    path('leercursos/', leerCursos, name='leerCursos'),
    path('entregables/', entregables, name='entregables'),
    #path('cursosFormulario/', CursoFormulario, name='cursosFormulario'),
    path('busquedaComision/', busquedaComision, name='busquedaComision'),
    path('buscar/', buscar, name='buscar'),
    path('eliminarProfesor/<nombre>', eliminarProfesor, name='eliminarProfesor'),
    path('editarProfesor/<nombre>', editarProfesor, name='editarProfesor'),
    path('eliminarEstudiante/<nombre>', eliminarEstudiante, name='eliminarEstudiante'),
    path('editarEstudiante/<nombre>', editarEstudiante, name='editarEstudiante'),
    path('eliminarCurso/<nombre>', eliminarCurso, name='eliminarCurso'),
    path('editarCurso/<nombre>', editarCurso, name='editarCurso'),
    



    path('estudiante/list/', EstudiantesList.as_view(), name='estudiante_listar'),
    path('estudiante/<pk>', EstudianteDetalle.as_view(), name='estudiante_detalle'),
    path('estudiante/nuevo/', EstudianteCreacion.as_view(), name='estudiante_crear'),
    path('estudiante/editar/<pk>', EstudianteEdicion.as_view(), name='estudiante_editar'),
    path('estudiante/borrar/<pk>', EstudianteEliminacion.as_view(), name='estudiante_borrar'),
]