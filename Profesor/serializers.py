from rest_framework import serializers
from Profesor.models import Profesor

from drf_dynamic_fields import DynamicFieldsMixin

class ProfesorSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Profesor
        fields = ('id','name', 'ap_pat','ap_mat','phone','age','gender','birth_date','years_experience')
