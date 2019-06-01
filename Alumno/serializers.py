from rest_framework import serializers
from Alumno.models import Alumno

from drf_dynamic_fields import DynamicFieldsMixin

class AlumnoSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Alumno
        fields = ('id','name','ap_pat', 'ap_mat','id_number','address','subject','phone','age','gender','birthdate','teacher')
