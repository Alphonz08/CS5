from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics


from Profesor.models import Profesor
from Profesor.serializers import ProfesorSerializer

class ProfesorList(APIView):
    def get (self, request, format=None):
        queryset = Profesor.objects.all()
        serializer = ProfesorSerializer(queryset, many=True, context = {'request': request})
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = ProfesorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    


# class ProfesorDetail(APIView):
#     def get_objetc(self, id):
#         try:
#             return Profesor.objects.get(pk=id)
#         except Profesor.DoesNotExist:
#             return 404

#     def get(self, request, id, format=None):
#         profe = self.get_objetc(id)
#         serializer = ProfesorSerializer(profe)
#         return Response(serializer.data)

class ProfesorDetail(APIView):
    def get_object(self, id):
        try:
            return Profesor.objects.get(pk=id)
        except Profesor.DoesNotExist:
            return "No"

    def get(self, request, id, format=None):
        Id = self.get_object(id)
        if Id != "No":
            Id = ProfesorSerializer(Id)
            return Response(Id.data)
        return Response("No existe")

    def put(self, request, id, format=None):
        Id = self.get_object(id)
        serializer = ProfesorSerializer(Id, data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response("Error", status=status.HTTP_400_BAD_REQUEST)