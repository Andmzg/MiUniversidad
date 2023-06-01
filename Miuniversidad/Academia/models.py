from django.db import models



class Carrera(models.Model):
    codigo = models.CharField(max_length=3, primary_key=True)
    nombre = models.CharField(max_length=50)
    duracion = models.PositiveSmallIntegerField(default=5)

    def __str__(self):
        txt = "{0} (Duracion: {1} years)"
        return txt.format(self.nombre, self.duracion)


class Estudiante(models.Model):
    dni = models.CharField(max_length=8, primary_key=True)
    apellidoPaterno = models.CharField(max_length=35)
    apellidomaterno = models.CharField(max_length=35)
    nombres = models.CharField(max_length=35)
    fechNacimiento = models.DateField()
    sexos = [
        ('F', 'Femenino'),
        ('M', 'Masculino')
    ]
    sexo = models.CharField(max_length=1, choices=sexos, default='F')
    carrera = models.ForeignKey(Carrera, null=False, blank=False, on_delete=models.CASCADE)
    vigencia = models.BooleanField(default=True)

    def nombrecompleto(self):
        txt = '{0} {1}, {2}'
        return txt.format(self.apellidoPaterno, self.apellidomaterno, self.nombres)

    def __str__(self):
        txt = "{0} / Carrera: {1} / {2}"
        if self.vigencia:
            estadoestudiante = "Vigente"
        else:
            estadoestudiante = "De baja"
        return txt.format(self.nombrecompleto(), self.carrera, estadoestudiante)


class Curso(models.Model):
    codigo = models.CharField(max_length=6, primary_key=True)
    nombre = models.CharField(max_length=30)
    creditos = models.PositiveSmallIntegerField()
    docente = models.CharField(max_length=100)

    def __str__(self):
        txt = "{0} ({1}) / Docente: {2} / Creditos: {3} "
        return txt.format(self.nombre, self.codigo, self.docente, self.creditos)


class Matricula(models.Model):
    estudiante = models.ForeignKey(Estudiante, null=False, blank=False, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, null=False, blank=False, on_delete=models.CASCADE)
    fechaMatricula = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        txt = "{0} matriculad{1} en el curso {2} / Fecha: {3}"
        if self.estudiante.sexo == "F":
            letrasexo = "a"
        else:
            letrasexo = "o"

        fech = self.fechaMatricula.strftime('%d-%m-%Y')
        return txt.format(self.estudiante.nombrecompleto(), letrasexo, self.curso, fech)
