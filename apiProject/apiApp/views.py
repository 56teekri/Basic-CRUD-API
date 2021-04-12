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
def get_student(request):
    id=request.data.get('id')
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
        return Response(response)
    else:
        return Response(serializer.errors)


@api_view(['PUT']) 
@csrf_exempt
def update_student(request):
    id=request.data.get('id')
    stu=models.Student.objects.get(id=id)
    data=request.data
    serializer=serializers.StudentSerializer(stu,data=data,partial=True)
    if(serializer.is_valid()):
        serializer.save()
        response={'msg':'data updated'}
        return Response(response)
    else:
        return Response(serializer.errors)

@api_view(['DELETE']) 
@csrf_exempt
def delete_student(request):
    id=request.data.get('id')
    stu=models.Student.objects.get(id=id)
    stu.delete()
    response={'msg':'data deleted'}
    return Response(response)