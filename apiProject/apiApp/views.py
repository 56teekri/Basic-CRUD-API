import io,json
from apiApp import models,serializers
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt


def get_student_data(request):
    if(request.method=='GET'):
        json_data=request.body
        stream=io.BytesIO(json_data)
        python_data=JSONParser().parse(stream)
        id=python_data.get('id',None)
        if(id is not None):
            stu=models.Student.objects.get(id=id)
            serializer=serializers.StudentSerializer(stu)
            return JsonResponse(serializer.data,safe=False)
        else:
            stu=models.Student.objects.all()
            serializer=serializers.StudentSerializer(stu,many=True)
            return JsonResponse(serializer.data,safe=False)



@csrf_exempt
def create_student(request):
    if(request.method=='POST'):
        json_data=request.body
        stream=io.BytesIO(json_data)
        python_data=JSONParser().parse(stream)
        serializer=serializers.StudentSerializer(data=python_data)
        if(serializer.is_valid()):
            serializer.save()
            response={'msg':'data created'}
            return JsonResponse(response,safe=False)
        else:
            return JsonResponse(serializer.errors,safe=False)


@csrf_exempt
def update_student(request):
    if(request.method=='PUT'):
        json_data=request.body
        stream=io.BytesIO(json_data)
        python_data=JSONParser().parse(stream)
        id=python_data.get('id')
        stu=models.Student.objects.get(id=id)
        serializer=serializers.StudentSerializer(stu,data=python_data,partial=True)
        if(serializer.is_valid()):
            serializer.save()
            response={'msg':'data updated'}
            return JsonResponse(response,safe=False)
        else:
            return JsonResponse(serializer.errors,safe=False)

@csrf_exempt
def delete_student(request):
    if(request.method=='DELETE'):
        json_data=request.body
        stream=io.BytesIO(json_data)
        python_data=JSONParser().parse(stream)
        id=python_data.get('id')
        stu=models.Student.objects.get(id=id)
        stu.delete()
        response={'msg':'data deleted'}
        return JsonResponse(response,safe=False)