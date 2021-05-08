from apiApp import models,serializers
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,UpdateModelMixin,RetrieveModelMixin,DestroyModelMixin

class StudentList(GenericAPIView,ListModelMixin):
    queryset=models.Student.objects.all()
    serializer_class=serializers.StudentSerializer
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

class StudentCreate(GenericAPIView,CreateModelMixin):
    queryset=models.Student.objects.all()
    serializer_class=serializers.StudentSerializer
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

class StudentRetrieve(GenericAPIView,RetrieveModelMixin):
    queryset=models.Student.objects.all()
    serializer_class=serializers.StudentSerializer
    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)

class StudentUpdate(GenericAPIView,UpdateModelMixin):
    queryset=models.Student.objects.all()
    serializer_class=serializers.StudentSerializer
    def get(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)

class StudentDelete(GenericAPIView,DestroyModelMixin):
    queryset=models.Student.objects.all()
    serializer_class=serializers.StudentSerializer
    def get(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)