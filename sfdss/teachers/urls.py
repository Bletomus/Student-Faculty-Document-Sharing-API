from django.urls import path
from teachers import views

urlpatterns = [
    path('validate_teacher/<int:person_id>',views.validate_teacher,name='validate_teacher'),
    path('get_faculty_details/<int:person_id>',views.get_faculty_details,name='get_faculty_details'),
    path('get_Teaches/<int:person_id>',views.get_Teaches,name='get_Teaches'),
    ]