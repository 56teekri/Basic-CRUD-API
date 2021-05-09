from django.shortcuts import render
from apiApp import models,serializers
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response


class StudentViewSet(viewsets.ViewSet):
    def list(self,request):
        stu=models.Student.objects.all()
        serializer=serializers.StudentSerializer(stu,many=True)
        return Response(serializer.data)
    
    def retrieve(self,request,pk=None):
        if(pk):
            stu=models.Student.objects.get(id=pk)
            serializer=serializers.StudentSerializer(stu)
            return Response(serializer.data)
    
    def create(self,request,pk=None):
        data=request.data
        serializer=serializers.StudentSerializer(data=data)
        if(serializer.is_valid()):
            serializer.save()
            msg={'msg':'data created'}
            return Response(msg,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def update(self,request,pk):
        data=request.data
        stu=models.Student.objects.get(pk=pk)
        serializer=serializers.StudentSerializer(stu,data=data)
        if(serializer.is_valid()):
            serializer.save()
            msg={'msg':'data created'}
            return Response(msg,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self,request,pk):
        data=request.data
        stu=models.Student.objects.get(pk=pk)
        serializer=serializers.StudentSerializer(stu,data=data,partial=True)
        if(serializer.is_valid()):
            serializer.save()
            msg={'msg':'data created'}
            return Response(msg,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def destroy(self,request,pk):
        stu=models.Student.objects.get(pk=pk)
        stu.delete()
        msg={'msg':'data deleted'}
        return Response(msg)













