from django.urls import path
from students import views

urlpatterns = [
    path('get_student_details/<int:person_id>',views.get_student_details,name='get_student_details'),
    #path('get_student_details/<int:person_id>',views.get_student_details,name='get_student_details'),
    ]