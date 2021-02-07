from rest_framework.decorators import api_view,parser_classes
from rest_framework.response import Response
from rest_framework import status
from resources.serializers import FacultyNotificationsSerializer,StudentNotificationsSerializer,UploadsSerializer
from resources.DatabaseAdapter import DatabaseAdapter
from resources.Constants import DatabaseConstants,ModelConstants
from rest_framework.parsers import FileUploadParser,MultiPartParser
from django.http import HttpResponse

from datetime import datetime
import logging
import hashlib
logger = logging.getLogger("mylogger")
timed = datetime.utcnow()
adapter = DatabaseAdapter()
constants = DatabaseConstants()
modalConstants= ModelConstants()
@api_view(['Get'])
def download_file(request,objectid):
    '''
    

    Parameters
    ----------
    request : TYPE
        DESCRIPTION.
    objectid : TYPE
        DESCRIPTION.

    Returns
    -------
    TYPE
        DESCRIPTION.

    '''
    
    try:
        
        uploads = adapter.getOneUpload(objectid)
        upload = uploads[2]
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    content1 = upload.file.read()
    content_type = upload.file.content_type
    logger.info(content_type)
    
    
    response = HttpResponse(content1,content_type =content_type)
    response['Content-Disposition'] = 'attachment; filename='+ upload.file_name
    
    return response
    
@api_view(['Get'])
def download_For_Notification_File(request,objectid):
    '''
    

    Parameters
    ----------
    request : TYPE
        DESCRIPTION.
    objectid : TYPE
        DESCRIPTION.

    Returns
    -------
    TYPE
        DESCRIPTION.

    '''
    try:
        
        uploads = adapter.getUploadForNotification(objectid)
        upload = uploads[2]
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    content1 = upload.file.read()
    content_type = upload.file.content_type
    response = HttpResponse(content1,content_type =content_type)
    response['Content-Disposition'] = 'attachment; filename='+ upload.file_name
    return response

@api_view(['Put','Post'])
@parser_classes([MultiPartParser])
def upload_file(request,person_id,sub_type,format = None):
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
   
        
    member = adapter.isMember(person_id)
    logger.info(person_id)
    
        
    
    logger.info(member)
    
 
    if member == True:
        
        if 'file' not in request.FILES:
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
        logger.info("file exist")
        f = request.FILES['file']
        file_name = f.name
        if f.size > modalConstants.max:
            return Response(status=status.HTTP_403_FORBIDDEN)
        logger.info("file is the write size")
        
        with f as fd:
            uploaded = adapter.writeUpload(file=fd,member=person_id,file_name=file_name,sub_type = sub_type)
        logger.info("upload is complete")
        if uploaded[0] == True:
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_422_UNPROCESSABLE_ENTITY)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['Put','Post'])
@parser_classes([MultiPartParser])
def upload_file_in_note(request,person_id):
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
        member = adapter.getFaculty(person_id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    stat = member[0]
    if stat == True:
        if 'file' not in request.data:
                return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
        logger.info("file exist")
        f = request.FILES['file']
        targetsString = request.data['targets']
        targetsList = (targetsString.strip()).split()
        # targetsLis = [x for x in targetsList if str.]
        targets = []
        logger.info(targetsString)
        logger.info(targetsList)
        for item in targetsList:
            logger.info(item)
            temp_var = int(item)
            targets.append(temp_var)
        dept =  request.data['dept']
        file_name = f.name
        if f.size > modalConstants.max:
            return Response(status=status.HTTP_403_FORBIDDEN)
        mem = member[2]
        with f as fd:
            logger.info(str(mem.id))
            uploaded = adapter.writeUpload(file=fd,member=str(mem.id),file_name=file_name,sub_type = 3)
        if uploaded[0] == True:
            upload = uploaded[1]
            name = "Upload Notification: " + str(hash(timed))
            note = mem.person_name + " has sent you a file. Please download the attached file to view what is in it!"
            students = [] 
            for item in targets:
                logger.info(item)
                obkect = adapter.getStudent(item)
                stu = obkect[2]
                students.append(stu)
            logger.info(len(students))
            dpt = adapter.getDepartment(dept)
            final_dept = dpt[2]
            result = adapter.createStudentNotifications(fac=mem,dept=final_dept,name=name,notification=note,upload=upload,targets=students,has_U = True)
            if result[0] == True:
                return Response(status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_422_UNPROCESSABLE_ENTITY)
            
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_409_CONFLICT)

@api_view(['Get'])
def get_faculty_notifications(request,person_id):
    '''
    

    Parameters
    ----------
    request : TYPE
        DESCRIPTION.
    person_id : TYPE
        DESCRIPTION.

    Returns
    -------
    TYPE
        DESCRIPTION.

    '''
    try:
        faculty_notifications = adapter.getFacultyNotifications(person_id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if faculty_notifications[0] == True:
        queryset = faculty_notifications[2]
        if len(queryset) > 0:
            if request.method == 'GET':
                serializer = FacultyNotificationsSerializer(queryset,many=True)
                return Response(serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
@api_view(['Get'])
def get_student_notifications(request,person_id):
    '''
    

    Parameters
    ----------
    request : TYPE
        DESCRIPTION.
    person_id : TYPE
        DESCRIPTION.

    Returns
    -------
    TYPE
        DESCRIPTION.

    '''
    try:
        student_notifications = adapter.getStudentNotifications(person_id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if student_notifications[0] == True:
        queryset = student_notifications[2]
        if len(queryset) > 0:
            if request.method == 'GET':
                serializer = StudentNotificationsSerializer(queryset,many=True)
                return Response(serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
@api_view(['Post'])
def get_Uploads(request):
    '''
    

    Parameters
    ----------
    request : TYPE
        DESCRIPTION.

    Returns
    -------
    TYPE
        DESCRIPTION.

    '''
    try:
        location = request.data.get('location')
    except:
         Response(status=status.HTTP_404_NOT_FOUND)
    logger.info(location)
    try:
        
        loci = hashlib.md5(location.encode()).hexdigest()
        logger.info(loci)
        uploads = adapter.getUpload(loci)
    except:
        Response(status=status.HTTP_404_NOT_FOUND)
    uploaded = uploads[0]
    if uploaded == True:
        logger.info(uploaded)
        queryset = uploads[2]
        if len(queryset) > 0:
            logger.info(len(queryset))
            
            logger.info("posties")
            serializer = UploadsSerializer(queryset,many=True)
            logger.info("posties")
            return Response(serializer.data)
        else:
            return Response([])
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)