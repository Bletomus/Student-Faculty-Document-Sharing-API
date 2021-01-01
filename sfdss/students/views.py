from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from resources.models import Students
from resources.serializers import StudentsSerializer
from mongoengine.errors import DoesNotExist
from resources.DatabaseAdapter import DatabaseAdapter
from django.http import HttpResponse
@api_view(['Get'])
def get_student_details(request,person_id):
    """
    get_student_details(person_id : LONG) takes a member id as a key and returns back their individual details
    
    Parameters
    ----------
    request : HTTP request
        Carries metadata on what the client wants the server to do as well as the type of method (GET,POST) the server must implement
    person_id : Long
        Persons number used to identify their record in the database

    Returns
    -------
    HttpResponse : JSON
        JSON file containing the information about the student if successful otherwise it will return file not found error(404) if the student is not registered in the database

    """
    try:
        students = Students.objects.get(student_number=person_id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = StudentsSerializer(students,)
        return Response(serializer.data)
    
    return Response({})

@api_view(['Get'])
def set_up_database(request):
    adapter = DatabaseAdapter()
    adapter.dropCollections()
    result = adapter.dummyInnitialize()
    
    if result[0] == True:
        return Response(status=status.HTTP_201_CREATED)
    
    return Response(status=status.HTTP_409_CONFLICT)
    
@api_view(['Get'])
def validate_student(request,person_id):
    """
    validate_student(person_id : LONG) takes a member id as a key and returns status code of whether or not a student is present
    
    Parameters
    ----------
    request : HTTP request
        Carries metadata on what the client wants the server to do as well as the type of method (GET,POST) the server must implement
    person_id : Long
        Persons number used to identify their record in the database

    Returns
    -------
    HttpResponse : Response
        return status code 302 if the student is present and 404 if otherwise

    """
    try:
        Students.objects.get(student_number=person_id)
    except DoesNotExist:
        return Response(data={},status=status.HTTP_404_NOT_FOUND)
    
    return Response(data={},status=status.HTTP_200_OK)
