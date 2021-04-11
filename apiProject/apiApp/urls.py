from django.urls import path
from apiApp import views
urlpatterns = [
    path('getdata',views.get_student_data,name='get_student_data'),
    path('createdata',views.create_student,name='create_student'),
    path('updatedata',views.update_student,name='update_student'),
    path('deletedata',views.delete_student,name='delete_student'),
]