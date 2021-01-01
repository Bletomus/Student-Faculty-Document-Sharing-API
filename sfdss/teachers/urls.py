from django.urls import path
from teachers import views

urlpatterns = [
    path('upload_file/<int:person_id>/<file_name>',views.upload_file,name='upload_file'),
    path('validate_teacher/<int:person_id>',views.validate_teacher,name='validate_teacher'),
    ]