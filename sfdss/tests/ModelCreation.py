# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 14:04:00 2020
from datetime import datetime
@author: Lee Flame
"""
from sfdss.models import *
from rest_framework.exceptions import ParseError
from datetime import datetime
time = datetime.utcnow()

class CreateModels:
    
    def __init__(self):
        Campus.drop_collection()
        Semesters.drop_collection()
        Courses.drop_collection()
        Departments.drop_collection()
        Building.drop_collection()
        Majors.drop_collection()
        Faculty.drop_collection()
        Students.drop_collection()
        CoursesPerMajor.drop_collection()
        StudentTakes.drop_collection()
        SemesterScores.drop_collection()
        SemesterSchedule.drop_collection()
        Notifications.drop_collection()
        Teaches.drop_collection()
        
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
        building = Building(building_campus = test_campus,building = "A",room_number = 101 )
        building.save()
        test_building = Building.objects().first()
        return test_building
    
    def createMajors(self,test_dept):
        major = Majors(major_department=test_dept,major="Comp")
        major.save()
        test_major = Majors.objects().first()
        return test_major
    
    def createStudent(self,test_major):
        time = datetime.utcnow()
        student = Students(student_name = "John",student_number = 1712510105,student_gender = "Male",student_nationality = "China",student_phone_number = [13071838053],student_major = test_major,id_type="Passport",enrollment_date=time,origin_country="China",place_of_birth="Harare")
        student.save()
        test_student = Students.objects().first()
        return test_student
    
    def createFaculty(self,test_major):
        faculty = Faculty(person_name = "Mr_Teacher",person_number = 972500105,phone_number = [13071838053,12334555],gender = "Male",nationality = "China",faculty_major = test_major)
        faculty.save()
        test_faculty = Faculty.objects().first()
        return test_faculty
    
    def createCoursesPerMajor(self,test_major,test_course):
        CPM = CoursesPerMajor(major_cpm=test_major,module =1,elective = False,course_cpm=test_course)
        CPM.save()
        test_cpm = CoursesPerMajor.objects().first()
        return test_cpm
    def createStudentTakes(self,ts,test_course,test_semester):
        st = StudentTakes(student_taking=ts,year=2020,course_taken=test_course,semester_taken=test_semester)
        st.save()
        test_st = StudentTakes.objects().first()
        return test_st
    
    def createGrading(self,student_taker,possible_major):
        grading = SemesterScores(student_took =student_taker,grade ="A",attempts = 1, score = 99.9,credits_ = 4)
        grading.save()
        test_grading = SemesterScores.objects().first()
        return test_grading
    
    def creatingSchedule(self, test_build,test_seme,test_maj,test_cos):
        sche = SemesterSchedule(scheduled_building = test_build,scheduled_year=2020,scheduled_semester=test_seme,scheduled_time=time,scheduled_major=test_maj,scheduled_course=test_cos)
        sche.save()
        test_sche = SemesterSchedule.objects().first()
        return test_sche 
    
    def createNotifications(self,fac,dept):
        note = Notifications(notification = "Hi sexy",type_ = "Emergency" ,note_time = time,registered_department = dept ,responible_faculty = fac)
        note.save()
        test_note = Notifications.objects().first()
        return test_note
    
    def createTeaches(self,fac,sch):
        teach = Teaches(teacher = fac,teacher_schedule=sch)
        teach.save()
        test_teach = Teaches.objects().first()
        return test_teach
    
    def createUploader(self,parser,uploada):
        pass
    
    def createStudentOP(self):
        test_campus = self.createCampus() 
        
        test_semester = self.createSemester() 
        
        test_course = self.createCouse() 
        
        test_dept =self.createDepartment()
        
        test_building = self.createBuilding(test_campus)
        
        test_major = self.createMajors(test_dept)
        
        test_student = self.createStudent(test_major)
    
        #return test_student