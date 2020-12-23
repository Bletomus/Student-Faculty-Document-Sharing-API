import json 
from rest_framework import status
from django.test import Client
from django.urls import reverse
from sfdss.models import *
from sfdss.serializers import StudentsSerializer
import unittest
from mongoengine import connect, disconnect
from sfdss.models import *
from tests.ModelCreation import CreateModels
from rest_framework.renderers import JSONRenderer
from resources.Constants import FakeDataBaseConstants

const_Fake_db = FakeDataBaseConstants()
client = Client()

class ViewTest(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        connect(db=const_Fake_db.db_Name, host=const_Fake_db.host, alias=const_Fake_db.alias)
        
    @classmethod
    def tearDownClass(cls):
        disconnect()
        
    def tests_(self):
        
        model = CreateModels()
        model.createStudentOP()
        response = client.get(reverse('get_student_details',kwargs={'person_id' : 1712510105}))
        student = Students.objects.get(person_number=1712510105)
        serializer = StudentsSerializer(student)
        str1 = "Your data is different buddy\n" + str(JSONRenderer().render(serializer.data)) + "\n vs \n" +str(JSONRenderer().render(response.data))
        
        assert response.data == serializer.data, str1