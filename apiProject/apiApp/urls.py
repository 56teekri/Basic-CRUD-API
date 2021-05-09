from django.contrib import admin
from django.urls import path,include
from apiApp import views
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register('studentapi',views.StudentViewSet,basename="student")
urlpatterns = [
    path("router/",include(router.urls))
]