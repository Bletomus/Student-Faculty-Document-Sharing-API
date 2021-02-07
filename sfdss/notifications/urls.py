from django.urls import path
from notifications import views

urlpatterns = [
    path('upload_file/<slug:person_id>/<int:sub_type>/',views.upload_file,name='upload_file'),
    path('get_faculty_notifications/<int:person_id>',views.get_faculty_notifications,name='get_faculty_notifications'),
    path('get_student_notifications/<int:person_id>',views.get_student_notifications,name='get_student_notifications'),
    path('get_Uploads/',views.get_Uploads,name='get_Uploads'),
    path('download_For_Notification_File/<objectid>',views.get_Uploads,name='download_For_Notification_File'),
    path('download_file/<objectid>',views.download_file,name='download_file'),
    path('upload_file_in_note/<int:person_id>',views.upload_file_in_note,name='upload_file_in_note'),
    ]