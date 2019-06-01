from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

class Profesor(models.Model):
    GENDER = [
        ('M','Masculino'),
        ('F','Femenino')
    ]
    name = models.CharField(max_length=100, null=False)
    ap_pat = models.CharField(max_length=100, null=False)
    ap_mat = models.CharField(max_length=100, null=False)
    phone = models.IntegerField(null=False)
    age = models.IntegerField(null=False)
    gender = models.CharField(
        max_length=1,
        choices= GENDER,
        null=False
    )
    birth_date = models.DateField(null=False)
    years_experience = models.IntegerField(null=False)
    delete = models.BooleanField(default = False)
    created = models.DateTimeField(default = timezone.now)
    edited = models.DateTimeField(blank=True, null=True, default=None)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Profesor'