from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics


from Alumno.models import Alumno
from Alumno.serializers import AlumnoSerializer

class AlumnoList(APIView):
    def get (self, request, format=None):
        queryset = Alumno.objects.all()
        serializer = AlumnoSerializer(queryset, many=True, context = {'request': request})
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = AlumnoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    


class AlumnoDetail(APIView):
    def get_objetc(self, id):
        try:
            return Alumno.objects.get(pk=id)
        except Alumno.DoesNotExist:
            return 404

    def get(self, request, id, format=None):
        alumno = self.get_objetc(id)
        serializer = AlumnoSerializer(alumno)
        return Response(serializer.data)