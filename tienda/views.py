from django.shortcuts import render, get_object_or_404
from .models import Programa, Curso, Estudiante


def home(request):
    return render(request, "academia/home.html", {})


# --- Programas ---
def lista_programas(request):
    programas = Programa.objects.all().order_by("nombre")
    return render(request, "academia/lista_programas.html", {"programas": programas})

def detalle_programa(request, pk):
    programa = get_object_or_404(Programa, pk=pk)
    return render(request, "academia/detalle_programa.html", {"programa": programa})


# --- Cursos ---
def lista_cursos(request):
    cursos = Curso.objects.all().order_by("nombre")
    return render(request, "academia/lista_cursos.html", {"cursos": cursos})

def detalle_curso(request, pk):
    curso = get_object_or_404(Curso, pk=pk)
    return render(request, "academia/detalle_curso.html", {"curso": curso})


# --- Estudiantes ---
def lista_estudiantes(request):
    estudiantes = Estudiante.objects.all().order_by("apellido")
    return render(request, "academia/lista_estudiantes.html", {"estudiantes": estudiantes})

def detalle_estudiante(request, pk):
    estudiante = get_object_or_404(Estudiante, pk=pk)
    return render(request, "academia/detalle_estudiante.html", {"estudiante": estudiante})