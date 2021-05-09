from apiApp import models,serializers
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView,ListCreateAPIView,RetrieveUpdateAPIView,RetrieveDestroyAPIView,RetrieveUpdateDestroyAPIView

class StudentList(ListAPIView):
    queryset=models.Student.objects.all()
    serializer_class=serializers.StudentSerializer

class StudentCreate(CreateAPIView):
    queryset=models.Student.objects.all()
    serializer_class=serializers.StudentSerializer

class StudentRetrieve(RetrieveAPIView):
    queryset=models.Student.objects.all()
    serializer_class=serializers.StudentSerializer

class StudentUpdate(UpdateAPIView):
    queryset=models.Student.objects.all()
    serializer_class=serializers.StudentSerializer

class StudentDelete(DestroyAPIView):
    queryset=models.Student.objects.all()
    serializer_class=serializers.StudentSerializer

class StudentListCreate(ListCreateAPIView):
    queryset=models.Student.objects.all()
    serializer_class=serializers.StudentSerializer

class StudentRetrieveUpdate(RetrieveUpdateAPIView):
    queryset=models.Student.objects.all()
    serializer_class=serializers.StudentSerializer

class StudentRetrieveDestroy(RetrieveDestroyAPIView):
    queryset=models.Student.objects.all()
    serializer_class=serializers.StudentSerializer


class StudentRetrieveDestroyUpdate(RetrieveUpdateDestroyAPIView):
    queryset=models.Student.objects.all()
    serializer_class=serializers.StudentSerializer





















