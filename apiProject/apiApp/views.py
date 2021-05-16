from django.shortcuts import render
from apiApp import models, serializers
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response


class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer
