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
    
# @api_view(['Get'])
# def uhhhhh(request):
    
#     try:
#         faculty = adapter.getFaculty(9725001001)
#     except:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     if faculty[0] ==True :
        
#         if request.method == 'GET':
#             item = faculty[2]
#             strr = item.person_name + "\n" + "\n" + item.gender + "\n" + item.nationality+ "\n" + item.faculty_major.major + "\n" 
#             return Response(strr)
#     else:
#         return Response(status=status.HTTP_404_NOT_FOUND)