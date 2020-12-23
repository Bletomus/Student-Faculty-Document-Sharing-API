# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 14:04:00 2020
from datetime import datetime
@author: Lee Flame
"""
from sfdss.models import *
from datetime import datetime

class CreateModels:
    time = datetime.utcnow()
    def __init__(self):
        Campus.drop_collection()
        Semesters.drop_collection()
        Courses.drop_collection()
        Departments.drop_collection()
        Building.drop_collection()
        Majors.drop_collection()
        Faculty.drop_collection()
        Students.drop_collection()
        
    def createCampus(self):
        campus = Campus(campus = "Jinshagang" )
        campus.save()
        test_campus = Campus.objects().first()
        return test_campus
    
    def createSemester(self):
        semester = Semesters(semester_number = 1,semester_name = "Summer" )
        semester.save()
        test_semester = Semesters.objects().first()
        return test_semester
    
    def createCouse(self):
        course_name = Courses(course_name = "example",course_id=1 )
        course_name.save()
        test_course = Courses.objects().first()
        return test_course
    
    def createDepartment(self):
        department_name = Departments(department_name = "SCIE" )
        department_name.save()
        test_dept = Departments.objects().first()
        return test_dept
    
    def createBuilding(self,test_campus):
        building = Building(campus = test_campus,building = "A",room_number = 101 )
        building.save()
        test_building = Building.objects().first()
        return test_building
    
    def createMajors(self,test_dept):
        major = Majors(department=test_dept,major="Comp")
        major.save()
        test_major = Majors.objects().first()
        return test_major
    
    def createStudent(self,test_major):
        time = datetime.utcnow()
        student = Students(person_name = "John",person_number = 1712510105,gender = "Male",nationality = "China",phone_number = [13071838053],major = test_major,id_type="Passport",enrollment_date=time,origin_country="China",place_of_birth="Harare")
        student.save()
        test_student = Students.objects().first()
        return test_student
    
    def createFaculty(self,test_major):
        faculty = Faculty(person_name = "Mr_Teacher",person_number = 972500105,phone_number = [13071838053,12334555],gender = "Male",nationality = "China",major = test_major)
        faculty.save()
        test_faculty = Faculty.objects().first()
        return test_faculty