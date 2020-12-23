import unittest
from mongoengine import connect, disconnect
from sfdss.models import *
from datetime import datetime

class ModelsTest(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        connect('mongoenginetest', host='mongomock://localhost', alias='testdb')
        
    @classmethod
    def tearDownClass(cls):
        
        disconnect()
    
    def test_thing(self):
        Campus.drop_collection()
        Semesters.drop_collection()
        Courses.drop_collection()
        Departments.drop_collection()
        Building.drop_collection()
        Majors.drop_collection()
        Faculty.drop_collection()
        Students.drop_collection()
        
        campus = Campus(campus = "Jinshagang" )
        campus.save()
        test_campus = Campus.objects().first()
        
        semester = Semesters(semester_number = 1,semester_name = "Summer" )
        semester.save()
        test_semester = Semesters.objects().first()
        
        course_name = Courses(course_name = "example",course_id=1 )
        course_name.save()
        test_course = Courses.objects().first()
        
        department_name = Departments(department_name = "SCIE" )
        department_name.save()
        test_dept = Departments.objects().first()
        
        """First Sanity Check on database for documents with no references"""
        assert test_campus.campus == "Jinshagang", "campus is wrong"
        
        assert test_semester.semester_name == "Summer" , "semester name is wrong"
        assert test_semester.semester_number == 1 , "semester number is wrong"
        
        assert test_course.course_name == "example","Course name is wrong"
        assert test_course.course_id == 1,"Course number is wrong"
        
        assert test_dept.department_name == "SCIE", "department name is wrong"
        
        """ Second Sanity Check on database for documents with references"""
        building = Building(campus = Campus.objects().first(),building = "A",room_number = 101 )
        building.save()
        test_building = Building.objects().first()
        
        assert test_building.campus ==  test_campus,"Campus is wrong"
        assert test_building.building ==  "A","Building name is wrong"
        assert test_building.room_number == 101 ,"Building number is wrong"
        
        """Third sanity check on database for the rest of the documents"""
        major = Majors(department=test_dept,major="Comp")
        major.save()
        test_major = Majors.objects().first()
        
        assert test_major.major == "Comp", "The major is missing"
        assert test_major.department == test_dept, "The department is missing"
        
        faculty = Faculty(person_name = "Mr_Teacher",person_number = 972500105,phone_number = [13071838053,12334555],gender = "Male",nationality = "China",major = test_major)
        faculty.save()
        test_faculty = Faculty.objects().first()
        
        assert test_faculty.person_name  == "Mr_Teacher", "Persons name is incorrect"
        assert test_faculty.person_number  == 972500105, "Persons number is incorrect"
        assert test_faculty.gender  == "Male", "Gender is incorrect"
        assert test_faculty.nationality  == "China", "Country is incorrect"
        assert test_faculty.phone_number  == [13071838053,12334555], "Number is incorrect"
        assert test_faculty.major  == test_major, "Major is incorrect"
        
        time = datetime.utcnow()
        student = Students(person_name = "John",person_number = 1712510105,gender = "Male",nationality = "China",phone_number = [13071838053],major = test_major,id_type="Passport",enrollment_date=time,origin_country="China",place_of_birth="Harare")
        student.save()
        test_student = Students.objects().first()
        
        assert test_student.person_name  == "John", "Persons name is incorrect"
        assert test_student.person_number  == 1712510105, "Persons number is incorrect"
        assert test_student.gender  == "Male", "Gender is incorrect"
        assert test_student.nationality  == "China", "Country is incorrect"
        assert test_student.phone_number  == [13071838053], "Number is incorrect"
        assert test_student.major  == test_major, "Major is incorrect"
        assert test_student.id_type  == "Passport", "Passport is incorrect"
        assert test_student.enrollment_date  == time, "Time is incorrect"
        assert test_student.origin_country  == "China", "Country is incorrect"
        assert test_student.place_of_birth  == Harare, "City is incorrect"
        
        