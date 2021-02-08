from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from resources.serializers import StudentsSerializer,StudentTakesSerializer,SemesterScoresSerializer,CoursesPerMajorSerializer,SemesterScheduleSerializer
from resources.DatabaseAdapter import DatabaseAdapter
adapter = DatabaseAdapter()

@api_view(['Get'])
def get_student_details(request,person_id):
    
    try:
        students = adapter.getStudent(person_id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if students[0] == True:
        if request.method == 'GET':
            serializer = StudentsSerializer(students[2],)
            return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['Get'])
def set_up_database(request):
    adapter.dropCollections()
    result = adapter.dummyInnitialize()
    
    if result[0] == True:
        return Response(status=status.HTTP_201_CREATED)
    
    return Response(status=status.HTTP_409_CONFLICT)
    
@api_view(['Get'])
def validate_student(request,person_id):
    
    try:
        student = adapter.getStudent(person_id)
    except:
        return Response(data={},status=status.HTTP_404_NOT_FOUND)
    
    if student[0] == True: 
        return Response(data={},status=status.HTTP_200_OK)
    else:
        return Response(data={},status=status.HTTP_404_NOT_FOUND)

@api_view(['Get'])
def get_Student_Takes(request,person_id):
    
    try:
        student = adapter.getStudentTakes(person_id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if student[0] == True:
        queryset = student[2]
        if len(queryset) > 0:
            if request.method == 'GET':
                serializer = StudentTakesSerializer(queryset,many=True)
                return Response(serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    
@api_view(['Get'])
def get_Student_Scores(request,person_id):
    
    try:
        student = adapter.getSemesterScores(person_id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if student[0] == True:
        queryset = student[2]
        if len(queryset) > 0:
            if request.method == 'GET':
                serializer = SemesterScoresSerializer(queryset,many=True)
                return Response(serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)    
    
    

@api_view(['Get'])
def get_Courses(request,person_id):
   
    try:
        student = adapter.getCPMByID(person_id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if student[0] == True:
        queryset = student[2]
        if len(queryset) > 0:
            if request.method == 'GET':
                serializer = CoursesPerMajorSerializer(queryset,many=True)
                return Response(serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['Get'])
def get_schedule(request,person_id):
   
    try:
        student_schedule = adapter.getScheduleByID(person_id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if student_schedule[0] == True:
        queryset = student_schedule[2]
        if len(queryset) > 0:
            if request.method == 'GET':
                serializer = SemesterScheduleSerializer(queryset,many=True)
                return Response(serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
