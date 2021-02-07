from rest_framework.decorators import api_view,parser_classes
from rest_framework.response import Response
from rest_framework import status
from resources.models import Uploads,Faculty
from resources.serializers import UploadsSerializer
from rest_framework.parsers import FileUploadParser
from rest_framework.exceptions import ParseError
from resources.DatabaseAdapter import DatabaseAdapter
from resources.Constants import DatabaseConstants
from resources.serializers import FacultySerializer,TeachesSerializer
from resources.DatabaseAdapter import DatabaseAdapter
from mongoengine.errors import DoesNotExist
constants = DatabaseConstants()
adapter = DatabaseAdapter()


@api_view(['Get'])
def validate_teacher(request,person_id):
    """
    validate_student(person_id : LONG) takes a member id as a key and returns status code of whether or not a teacher is present
    
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
        faculty = adapter.getFaculty(person_id)
    except:
        return Response(data={},status=status.HTTP_404_NOT_FOUND)
    
    if faculty[0] == True: 
        return Response(data={},status=status.HTTP_200_OK)
    else:
        return Response(data={},status=status.HTTP_404_NOT_FOUND)

@api_view(['Get'])
def get_faculty_details(request,person_id):
    """
    get_faculty_details(person_id : LONG) takes a member id as a key and returns back their individual details
    
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
        faculty = adapter.getFaculty(person_id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if faculty[0] ==True :
        
        if request.method == 'GET':
            serializer = FacultySerializer(faculty[2],)
            return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
@api_view(['Get'])
def get_Teaches(request,person_id):
    '''
    

    Parameters
    ----------
    request : TYPE
        DESCRIPTION.
    person_id : Integer
        DESCRIPTION.

    Returns
    -------
    TYPE
        DESCRIPTION.

    '''
    try:
        faculty = adapter.getTeaches(person_id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if faculty[0] ==True :
        queryset = faculty[2]
        if len(queryset) > 0:
            
            if request.method == 'GET':
                serializer = TeachesSerializer(queryset,many=True)
                return Response(serializer.data)
        else:
            Response(status=status.HTTP_404_NOT_FOUND)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
@api_view(['Get'])
def uhhhhh(request):
    
    try:
        faculty = adapter.getFaculty(9725001001)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if faculty[0] ==True :
        
        if request.method == 'GET':
            item = faculty[2]
            strr = item.person_name + "\n" + "\n" + item.gender + "\n" + item.nationality+ "\n" + item.faculty_major.major + "\n" 
            return Response(strr)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)