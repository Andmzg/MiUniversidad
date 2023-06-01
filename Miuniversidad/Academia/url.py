from django.urls import path

from . import views

app_name = "academia"

urlpatterns = [
    path("formulario/", views.formulariocontacto, name="formulario"),
    path("exitoso/", views.contactar, name="exitoso"),
    path("cursos/", views.cursos, name="cursos"),
    path("registarCurso/", views.registrarcursos, name="registrarcursos"),
    path("eliminacionCurso/<codigo>", views.eliminarcurso, name="eliminarcurso"),
    path("editcurso/<codigo>", views.editcurso, name="editcurso"),
    path("edit/", views.edit, name="edit"),
    path("list/", views.get_courses, name="list"),

]
