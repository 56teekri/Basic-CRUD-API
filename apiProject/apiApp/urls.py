from django.contrib import admin
from django.urls import path
from apiApp import views
urlpatterns = [
    path('listget',views.StudentList.as_view()),
    path('oneget/<int:pk>',views.StudentRetrieve.as_view()),
    path('create',views.StudentCreate.as_view()),
    path('update/<int:pk>',views.StudentUpdate.as_view()),
    path('delete/<int:pk>',views.StudentDelete.as_view()),
    path('listcreate',views.StudentListCreate.as_view()),
    path('retrieveupdate/<int:pk>',views.StudentRetrieveUpdate.as_view()),
    path('retrievedestroy/<int:pk>',views.StudentRetrieveDestroy.as_view()),
    path('retrievedestroyupdate/<int:pk>',views.StudentRetrieveDestroyUpdate.as_view()),
]