import json 
from rest_framework import status
from django.test import Client
from django.urls import reverse
from resources.models import *
from resources.serializers import StudentsSerializer
import unittest
from mongoengine import connect, disconnect
from resources.models import *
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
        
        upload_payload = {'file':1}
        
        model.createStudentOP()

        response = client.get(reverse('get_student_details',kwargs={'person_id' : 1712510105}))
        student = Students.objects.get(student_number=1712510105)
        serializer = StudentsSerializer(student)
        str1 = "Your data is different buddy\n" + str(JSONRenderer().render(serializer.data)) + "\n vs \n" +str(JSONRenderer().render(response.data))
        
        assert response.data == serializer.data, str1
        
        #response = client.put(reverse('get_post_puppies',kwargs={'person_id' : 972500105,'file_name':"test_file"}),data=payload,content_type='application/json')
        
        response_2 = client.get(reverse('validate_student',kwargs={'person_id' : 1712510105}))
        response_3 = client.get(reverse('validate_student',kwargs={'person_id' : 1712510115}))
        assert response_2.status_code == 200, "The code is wrong"
        assert response_3.status_code == 404, "The code is correct"
        
        response_5 = client.get(reverse('set_up_database',kwargs={}))
        
        assert response_5.status_code == 201,"Error somewhere"