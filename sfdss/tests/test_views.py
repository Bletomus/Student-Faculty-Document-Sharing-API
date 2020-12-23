import json 
from rest_framework import status
from django.test import Client
from django.urls import reverse
from sfdss.models import *
#from sfdss.serializers import StudentsSerializer
import unittest
from mongoengine import connect, disconnect
from sfdss.models import *


client = Client()

class ViewTest(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        connect('mongoenginetest', host='mongomock://localhost', alias='testdb')
        
    @classmethod
    def tearDownClass(cls):
        disconnect()
        
    def tests_(self):
        
        response = client.get(reverse('get_student_details',kwargs={'person_id' : 1712510105}))
        student = Students.objects(person_number=1712510105)
        #serializer = StudentsSerializer(student)
        str1 = "Your data is different buddy"
        for st in student:
            str1 =  str1 + st.person_name
            
        assert 1 == 2, str1