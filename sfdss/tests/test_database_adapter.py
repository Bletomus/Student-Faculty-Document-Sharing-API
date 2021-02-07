import json 
from rest_framework import status
from django.test import Client
from django.urls import reverse
from resources.models import *
from resources.serializers import StudentsSerializer
import unittest
from mongoengine import connect, disconnect
from resources.models import *
from resources.DatabaseAdapter import DatabaseAdapter
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
        adapter = DatabaseAdapter()
        adapter.dropCollections()
        # """Campus test"""
        # response_1 = adapter.createCampus("Jinshagang")
        
        # response_2 = adapter.createCampus("Jinshagang")
        
        # assert response_1[0] == True, "it didnt go in all is not well"
        # assert response_2[0] == False, "okay that waas supposed to be unique"
        
        # campus_done = adapter.getCampus("Jinshagang")
        
        # assert campus_done[0] == True, "something went wrong"
        
        # """Semester Test"""
        
        # response_3 = adapter.createSemester("Winter",1)
        
        # response_4 = adapter.createSemester("Winter",1)
        
        # assert response_3[0] == True, "it didnt go in all is not well"
        # assert response_4[0] == False, "okay that waas supposed to be unique"
        
        # semester_done = adapter.getSemester("Winter")
        
        # assert semester_done[0] == True, "something went wrong"
        
        # """Courses Test"""
        # response_5 = adapter.createCourse("Intro To Comp Sci",2323)
        
        # response_6 = adapter.createCourse("Intro To Comp Sci",2323)
        
        # assert response_5[0] == True, "it didnt go in all is not well"
        # assert response_6[0] == False, "okay that waas supposed to be unique"
        
        # course_done = adapter.getCourse(2323)
        
        # assert course_done[0] == True, "something went wrong"
        
        # """Departments Test"""
        # response_7 = adapter.createDepartment("SCIE")
        
        # response_8 = adapter.createDepartment("SCIE")
        
        # assert response_7[0] == True, "it didnt go in all is not well"
        # assert response_8[0] == False, "okay that waas supposed to be unique"
        
        # dept_done = adapter.getDepartment("SCIE")
        # assert dept_done[0] == True, "something went wrong"
        
        # """Building Test"""
        # response_9 = adapter.createBuilding(campus = campus_done[2], building_name="A", room =101)
        
        # response_10 = adapter.createBuilding(campus = campus_done[2], building_name="A", room =101)
        
        # assert response_9[0] == True, "it didnt go in all is not well"
        # assert response_10[0] == False, "okay that waas supposed to be unique"
        
        # building_done = adapter.getBuilding("A")
        
        # assert building_done[0] == True, "something went wrong"
        
        # """Majors Test"""
        # response_11 = adapter.createMajors(dept = dept_done[2], major_name="Computer Science")
        
        # response_12 = adapter.createMajors(dept = dept_done[2], major_name="Computer Science")
        
        # assert response_11[0] == True, "it didnt go in all is not well"
        # assert response_12[0] == False, "okay that waas supposed to be unique"
        
        # majors_done = adapter.getMajors("Computer Science")
        
        # assert majors_done[0] == True, "something went wrong"
        
        # """Faculty Test"""
        # response_13 = adapter.createFaculty(name = "Mr_Teacher", number =9725001005,major= majors_done[2])
        
        # response_14 = adapter.createFaculty(name = "Mr_Teacher", number =9725001005,major= majors_done[2])
        
        # assert response_13[0] == True, "it didnt go in all is not well"
        # assert response_14[0] == False, "okay that waas supposed to be unique"
        
        # faculty_done = adapter.getFaculty(9725001005)
        
        # assert faculty_done[0] == True, "something went wrong"
        
        # """Students Test"""
        # response_15 = adapter.createStudent(name = "Mr_Teacher", number =1712510101,major= majors_done[2])
        
        # response_16 = adapter.createStudent(name = "Mr_Teacher", number =1712510101,major= majors_done[2])
        
        # assert response_15[0] == True, "it didnt go in all is not well"
        # assert response_16[0] == False, "okay that waas supposed to be unique"
        
        # student_done = adapter.getStudent(1712510101)
        
        # assert student_done[0] == True, "something went wrong"
        
        # """Student Takes Test"""
        # response_17 = adapter.createStudentTakes(year=2020,student=student_done[2],course=course_done[2],semester = semester_done[2])
        
        # response_18 = adapter.createStudentTakes(year=2020,student=student_done[2],course=course_done[2],semester = semester_done[2])
        
        # assert response_17[0] == True, "it didnt go in all is not well"
        # assert response_18[0] == False, "okay that waas supposed to be unique"
        
        # student_takes_done = adapter.getStudentTakes(1712510101)
        
        # assert student_takes_done[0] == True, "something went wrong"
        
        # """Semester Scores"""
        # testa = student_takes_done[2]
        # first = testa[0]
        # response_19 = adapter.createSemesterScores(first)
        
        # response_20 = adapter.createSemesterScores(first)
        
        # assert response_19[0] == True, "it didnt go in all is not well"
        # assert response_20[0] == False, "okay that waas supposed to be unique"
        
        # student_fails = adapter.getSemesterScores(1712510101)
        
        # assert student_fails[0] == True, "something went wrong"
        
        # """Courses Per Major Text"""
        # response_21 = adapter.createCPM(major=majors_done[2],course =course_done[2],semester=semester_done[2])
        
        # response_22 = adapter.createCPM(major=majors_done[2],course =course_done[2],semester=semester_done[2])
        
        # assert response_21[0] == True, "it didnt go in all is not well"
        # assert response_22[0] == False, "okay that waas supposed to be unique"
        # maj = majors_done[2]
        # cpm_done = adapter.getCPM(maj)
        
        # assert cpm_done[0] == True, "something went wrong"
        
        # """Semester Schedule"""
        # response_23 = adapter.createSchedule(building=building_done[2],semester=semester_done[2],major=majors_done[2],course=course_done[2])
        
        # response_24 = adapter.createSchedule(building=building_done[2],semester=semester_done[2],major=majors_done[2],course=course_done[2])
        
        # assert response_23[0] == True, "it didnt go in all is not well"
        # assert response_24[0] == False, "okay that waas supposed to be unique"
        # maj = majors_done[2]
        # ss_done = adapter.getSchedule(maj)
        
        # assert ss_done[0] == True, "something went wrong"
        
        # """Teaches"""
        # st = Students.objects.all()
        # stlist = [item for item in st]
        # sch = SemesterSchedule.objects[0]
        
        # response_25 = adapter.createTeaches(teacher=faculty_done[2],schedule=sch,students=stlist)
        
        # response_26 = adapter.createTeaches(teacher=faculty_done[2],schedule=sch,students=stlist)
        
        # assert response_25[0] == True, "it didnt go in all is not well"
        # assert response_26[0] == False, "okay that waas supposed to be unique"
        
        # teaches_done = adapter.getTeaches(9725001005)
        
        # assert teaches_done[0] == True, "something went wrong"
        
        # """Notifications"""
        # response_27 = adapter.createFacultyNotifications(upload="",fac=faculty_done[2],dept=dept_done[2],name="Tupac",notification="I love you doc")
        
        # response_28 = adapter.createFacultyNotifications(upload="",fac=faculty_done[2],dept=dept_done[2],name="Tupac",notification="I love you doc")
        
        # assert response_27[0] == True, "it didnt go in all is not well"
        # assert response_28[0] == False, "okay that waas supposed to be unique"
        
        # fn_done = adapter.getFacultyNotifications(9725001005)
        
        # assert fn_done[0] == True, "something went wrong"
        
        # """Student Notifications"""
        
        # response_29 = adapter.createStudentNotifications(upload="",fac=faculty_done[2],dept=dept_done[2],name="upac",notification="I love you doc")
        # targets = []
        # adapter.createStudent(name = "Mr_Teacher", number =1712510102,major= majors_done[2])
        
        # targets.append(student_done[2])
        # #targets.append(Students.objects[1])
        # response_30 = adapter.createStudentNotifications(upload="",fac=faculty_done[2],dept=dept_done[2],name="Drake",notification="I love you doc",targets=targets)
        
        # assert response_29[0] == True, "it didnt go in all is not well"
        # assert response_30[0] == True, "okay that waas supposed to be unique"
        
        # sn_done = adapter.getStudentNotifications(1712510101)
        
        # assert sn_done[0] == True, "something went wrong"
        up_done = adapter.getUpload(1223456)
        assert up_done[0] ==True,"something wrong somewhere"
        # adapter.dropCollections()
        # response_15 = adapter.dummyInnitialize()
        
        
        # assert response_15[0] == True, response_15[1]
        
        # response = adapter.getCPMByID(1712510101)
        
        # assert response[0] == True, response[1]
        
        # response_1 = adapter.getScheduleByID(1712510101)
        
        # assert response_1[0] == True, response_1[1]