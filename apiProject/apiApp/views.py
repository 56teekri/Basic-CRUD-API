import io,json
from apiApp import models,serializers
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET'])
def get_student(request,pk=None):
    id=pk
    if(id is not None):
        stu=models.Student.objects.get(id=id)
        serializer=serializers.StudentSerializer(stu)
        return Response(serializer.data)
    else:
        stu=models.Student.objects.all()
        serializer=serializers.StudentSerializer(stu,many=True)
        return Response(serializer.data)

@api_view(['POST']) 
@csrf_exempt
def create_student(request):
    data=request.data
    serializer=serializers.StudentSerializer(data=data)
    if(serializer.is_valid()):
        serializer.save()
        response={'msg':'data created'}
        return Response(response,status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT','PATCH']) 
@csrf_exempt
def update_student(request,pk=None):
    if(request.method=='PUT'):
        id=pk
        stu=models.Student.objects.get(id=id)
        data=request.data
        serializer=serializers.StudentSerializer(stu,data=data)
        if(serializer.is_valid()):
            serializer.save()
            response={'msg':'complete data updated'}
            return Response(response)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    if(request.method=='PATCH'):
        id=pk
        stu=models.Student.objects.get(id=id)
        data=request.data
        serializer=serializers.StudentSerializer(stu,data=data,partial=True)
        if(serializer.is_valid()):
            serializer.save()
            response={'msg':'partial data updated'}
            return Response(response)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@csrf_exempt
def delete_student(request,pk=None):
    id=pk
    stu=models.Student.objects.get(id=id)
    stu.delete()
    response={'msg':'data deleted'}
    return Response(response)