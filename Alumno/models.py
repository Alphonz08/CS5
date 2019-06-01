from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

class Alumno(models.Model):
    MATERIAS = [
        ('PCS', 'Programacion cliente servidor'),
        ('SID', 'Sistemas digitales'),
        ('ARS', 'Arquitectura de software'),
        ('FUR', 'Fundamentos de redes'),
    ]
    GENDER = [
        ('M','Masculino'),
        ('F','Femenino')
    ]
    name = models.CharField(max_length=100, null=False)
    ap_pat = models.CharField(max_length=100, null=False)
    ap_mat = models.CharField(max_length=100, null=False)
    id_number = models.IntegerField(null=False)
    address = models.CharField(max_length=100, null=False)
    subject = models.CharField(
        max_length=3,
        choices=MATERIAS,
        default='PCS',)
    phone = models.IntegerField(null=False)
    age = models.IntegerField(null=False)
    gender = models.CharField(
        max_length=1,
        choices= GENDER,
        null=False
    )
    birthdate = models.DateField(null=False)
    teacher = models.ForeignKey('Profesor.Profesor', on_delete=models.SET(-1))
    delete = models.BooleanField(default = False)
    created = models.DateTimeField(default = timezone.now)
    edited = models.DateTimeField(blank=True, null=True, default=None)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Alumno'