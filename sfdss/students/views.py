from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from sfdss.models import Students
from sfdss.serializers import StudentsSerializer

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
        students = Students.objects.get(student_name=person_id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = StudentsSerializer(students,)
        return Response(serializer.data)
    
    return Response({})



