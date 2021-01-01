from django.urls import path
from students import views

urlpatterns = [
    path('validate_student/<int:person_id>',views.validate_student,name = 'validate_student'),
    path('get_student_details/<int:person_id>',views.get_student_details,name='get_student_details'),
    path('set_up_database/',views.set_up_database,name = 'set_up_database'),
    #path('get_student_details/<int:person_id>',views.get_student_details,name='get_student_details'),
    ]