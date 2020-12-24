from sfdss.models import *
from resources.Constants import ModelConstants
from datetime import datetime
import mimetypes

time = datetime.utcnow()

"""
Module containing the classes necessary to input and retrieve data from the database for the api to work
Classes
----------
DatabaseAdapter
    Contains the functions to input and retrieve data from the database
"""
constants = ModelConstants()
class DatabaseAdapter:
    """
    Contains the functions to input and retrieve data from the database
    
    Functions
    ----------
    writeUpload(file : FILE,member : Faculty) writes the file uploads and relevant information into the database Uploads model
    createLocationTuple(member : Teaches,sub_type :Integer) will be used to generate a string name for the location of the file the user will upload
    
    """
    
    def __init__(self):
        pass
    
    def writeUpload(self,file,member,file_name,sub_type = 1):
        """
        def writeUpload(file : FIL,member : Faculty) writes the file uploads and relevant information into the database Uploads model

        Parameters
        ----------
        file : FILE
            File that will be uploaded to the database
        member : tEACHES
            Teaches document class that will be inputed along the uploaded file to identify the person who uploaded the file and the course to upload under
        file_name : String
            Name of the file used to identify the file in the database
        Returns
        -------
        upload : Uploads
            Return the uploads model of the recently created file

        """
        
        location = self.createLocationTuple(member,sub_type)
        upload = Uploads(file_name=file_name,location = location,uploader=member,upload_time=time)
        upload.file.put(file, content_type = mimetypes.guess_type(file_name)[0])
        upload.save()
        return upload
    
    def createLocationTuple(self,member,sub_type):
        """
        createLocationTuple(member : Teaches,sub_type :Integer) will be used to generate a string name for the location of the file the user will upload

        Parameters
        ----------
        member : Teaches
            Contains a document with the relevant information to create a file location

        Returns
        -------
        location : tuple of strings
            The strings that will be used to identify the file

        """
        dept = str(member.teacher_schedule.scheduled_major.major_department)
        major = str(member.teacher_schedule.scheduled_major.major)
        course = str(member.teacher_schedule.scheduled_course.course_name)
        teach = str(member.teacher.person_name)
        semester = str(member.teacher_schedule.scheduled_semester.semester_name)
        sub_type = str(constants.submission_type[sub_type])
        location = " ".join((dept,major,course,teach,semester,sub_type))
        return location
        