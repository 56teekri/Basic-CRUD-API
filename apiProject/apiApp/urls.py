from django.contrib import admin
from django.urls import path
from apiApp import views
urlpatterns = [
    path('listget',views.StudentList.as_view()),
    path('oneget/<int:pk>',views.StudentRetrieve.as_view()),
    path('create',views.StudentCreate.as_view()),
    path('update/<int:pk>',views.StudentUpdate.as_view()),
    path('delete/<int:pk>',views.StudentDelete.as_view()),
]