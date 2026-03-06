from django.db import models


class Programa(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre


class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=20, unique=True)
    programa = models.ForeignKey(Programa, on_delete=models.CASCADE, related_name="cursos")

    def __str__(self):
        return f"{self.codigo} - {self.nombre}"


class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    codigo_estudiantil = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Inscripcion(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, related_name="inscripciones")
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name="inscripciones")
    fecha_inscripcion = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("estudiante", "curso")  # Regla de negocio: no duplicados

    def __str__(self):
        return f"{self.estudiante} → {self.curso}"