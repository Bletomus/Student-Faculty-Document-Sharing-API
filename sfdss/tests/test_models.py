import unittest
from mongoengine import connect, disconnect
from sfdss.models import *
from datetime import datetime
from tests.ModelCreation import CreateModels

class ModelsTest(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        connect('mongoenginetest', host='mongomock://localhost', alias='testdb')
        
    @classmethod
    def tearDownClass(cls):
        
        disconnect()
    
    def test_thing(self):
        
        
        model = CreateModels()
        
        test_campus = model.createCampus() 
        
        test_semester = model.createSemester() 
        
        test_course = model.createCouse() 
        
        test_dept =model.createDepartment()
        
        """First Sanity Check on database for documents with no references"""
        assert test_campus.campus == "Jinshagang", "campus is wrong"
        
        assert test_semester.semester_name == "Summer" , "semester name is wrong"
        assert test_semester.semester_number == 1 , "semester number is wrong"
        
        assert test_course.course_name == "example","Course name is wrong"
        assert test_course.course_id == 1,"Course number is wrong"
        
        assert test_dept.department_name == "SCIE", "department name is wrong"
        
        """ Second Sanity Check on database for documents with references"""

        test_building = model.createBuilding(test_campus)
        
        assert test_building.campus ==  test_campus,"Campus is wrong"
        assert test_building.building ==  "A","Building name is wrong"
        assert test_building.room_number == 101 ,"Building number is wrong"
        
        """Third sanity check on database for the rest of the documents"""

        test_major = model.createMajors(test_dept)
        
        assert test_major.major == "Comp", "The major is missing"
        assert test_major.department == test_dept, "The department is missing"
        
        test_faculty = model.createFaculty(test_major)
        
        assert test_faculty.person_name  == "Mr_Teacher", "Persons name is incorrect"
        assert test_faculty.person_number  == 972500105, "Persons number is incorrect"
        assert test_faculty.gender  == "Male", "Gender is incorrect"
        assert test_faculty.nationality  == "China", "Country is incorrect"
        assert test_faculty.phone_number  == [13071838053,12334555], "Number is incorrect"
        assert test_faculty.major  == test_major, "Major is incorrect"
        
        time = datetime.utcnow()
        test_student = model.createStudent(test_major)
        
        assert test_student.person_name  == "John", "Persons name is incorrect"
        assert test_student.person_number  == 1712510105, "Persons number is incorrect"
        assert test_student.gender  == "Male", "Gender is incorrect"
        assert test_student.nationality  == "China", "Country is incorrect"
        assert test_student.phone_number  == [13071838053], "Number is incorrect"
        assert test_student.major  == test_major, "Major is incorrect"
        assert test_student.id_type  == "Passport", "Passport is incorrect"
        assert test_student.enrollment_date  == time, "Time is incorrect"
        assert test_student.origin_country  == "China", "Country is incorrect"
        assert test_student.place_of_birth  == "Harare", "City is incorrect"
        
        