from rest_framework.decorators import api_view,parser_classes
from rest_framework.response import Response
from rest_framework import status
from sfdss.models import Uploads,Faculty
from sfdss.serializers import UploadsSerializer
from rest_framework.parsers import FileUploadParser
from rest_framework.exceptions import ParseError
from sfdss.DatabaseAdapter import DatabaseAdapter
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
        faculty_member = Faculty.objects.get(person_name = person_id)
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