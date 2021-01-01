from rest_framework.decorators import api_view,parser_classes
from rest_framework.response import Response
from rest_framework import status
from resources.models import Uploads,Faculty
from resources.serializers import UploadsSerializer
from rest_framework.parsers import FileUploadParser
from rest_framework.exceptions import ParseError
from resources.DatabaseAdapter import DatabaseAdapter
from resources.Constants import DatabaseConstants
constants = DatabaseConstants()

@api_view(['Put'])
@parser_classes([FileUploadParser])
def upload_file(request,person_id,file_name):
    """
    upload_file(person_id : LONG,file_name : STRING) takes a member id and parses the uploaded file, under the registered member, into the database
    

    Parameters
    ----------
    request : HTTP request
        Constains the posted data to be uploaded into the database including the file to be uploaded
    person_id : Long
        Persons number used to identify their record in the database
    file_name : String
        Contains the name of the file with underscores
        
    Returns
    -------
    HttpResponse : JSON
        JSON file containing the information about the uploaded file

    """
    try:
        faculty_member = Faculty.objects.get(person_number = person_id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if 'file' not in request.data:
            raise ParseError("Empty content")
    
    f = request.data['file']
    
    if f.size > constants.max:
        raise ParseError("File is too large")
        
    adapter = DatabaseAdapter() 
    with f as fd:
        uploaded = adapter.writeUpload(file=f,member=faculty_member,file_name=file_name)
    
    return Response({})

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
        faculty = Faculty.objects.get(person_number=person_id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    return Response(status=status.HTTP_302_FOUND)