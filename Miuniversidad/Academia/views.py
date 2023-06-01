from django.shortcuts import render, redirect
from django.conf import settings
from django.core.mail import send_mail
from .models import Curso
from django.contrib import messages
from django.http import JsonResponse


def formulariocontacto(request):
    return render(request, "academia/form.html")


def contactar(request):
    if request.method == "POST":
        asunto = request.POST["Asunto"]
        mensaje = request.POST["Mensaje"] + " / Email: " + request.POST["Email"]
        email_desde = settings.EMAIL_HOST_USER
        email_para = ["richardmj67@gmail.com"]
        send_mail(asunto, mensaje, email_desde, email_para, fail_silently=False)
        return render(request, "academia/contactoexitodo.html")
    return render(request, "form.html")


def cursos(request):
    cursosListados = Curso.objects.all()
    return render(request, "academia/gestionCursos.html", {"cursosListados":cursosListados})


def registrarcursos(request):
    codigo=request.POST["txtcodigo"]
    nombre=request.POST["txtnombre"]
    creditos=request.POST["txtcreditos"]
    docente=request.POST["txtdocente"]

    if codigo in Curso.objects.values_list('codigo', flat='True'):
        messages.success(request, "El codigo ya esta registrado. Ingrese un codigo diferente.")
    else:
        curso = Curso.objects.create(codigo=codigo, nombre=nombre, creditos=creditos, docente=docente)
        messages.success(request, "Curso agregado!")
    return redirect("academia:cursos")

def eliminarcurso(request, codigo):
    curso = Curso.objects.get(codigo=codigo)
    curso.delete()
    messages.success(request, "Curso eliminado!")
    return redirect("academia:cursos")

def editcurso(request, codigo):
    cursos_nombres = Curso.objects.values_list("nombre", flat= True).distinct()
    cursos_docentes = Curso.objects.values_list("docente", flat= True).distinct()
    curso = Curso.objects.get(codigo=codigo)
    context = {'curso': curso, 'cursos_nombres': cursos_nombres, 'cursos_docentes': cursos_docentes}
    return render(request, "academia/edicion.html", context)

def edit(request):
    codigo=request.POST["txtcodigo"]
    nombre=request.POST["txtnombre"]
    creditos=request.POST["txtcreditos"]
    docente=request.POST["txtdocente"]
    
    curso = Curso.objects.get(codigo=codigo)
    curso.nombre = nombre
    curso.creditos = creditos
    curso.docente = docente
    curso.save()
    messages.success(request, "Curso editado!")
    return redirect("academia:cursos")
    
def get_courses(request):
    cursos = Curso.objects.all()
    data = {'courses': [{'codigo': curso.codigo, 'nombre': curso.nombre} for curso in cursos]}
    return JsonResponse(data)