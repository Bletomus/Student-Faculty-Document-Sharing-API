import unittest
from mongoengine import connect, disconnect
from sfdss.models import *
from datetime import datetime
from tests.ModelCreation import CreateModels
from resources.Constants import FakeDataBaseConstants
from rest_framework.parsers import FileUploadParser

const_Fake_db = FakeDataBaseConstants()

class ModelsTest(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        connect(db=const_Fake_db.db_Name, host=const_Fake_db.host, alias=const_Fake_db.alias)
        
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
        
        assert test_building.building_campus ==  test_campus,"Campus is wrong"
        assert test_building.building ==  "A","Building name is wrong"
        assert test_building.room_number == 101 ,"Building number is wrong"
        
        """Third sanity check on database for the rest of the documents"""

        test_major = model.createMajors(test_dept)
        
        assert test_major.major == "Comp", "The major is missing"
        assert test_major.major_department == test_dept, "The department is missing"
        
        test_faculty = model.createFaculty(test_major)
        
        assert test_faculty.person_name  == "Mr_Teacher", "Persons name is incorrect"
        assert test_faculty.person_number  == 972500105, "Persons number is incorrect"
        assert test_faculty.gender  == "Male", "Gender is incorrect"
        assert test_faculty.nationality  == "China", "Country is incorrect"
        assert test_faculty.phone_number  == [13071838053,12334555], "Number is incorrect"
        assert test_faculty.faculty_major  == test_major, "Major is incorrect"
        
        time = datetime.utcnow()
        test_student = model.createStudent(test_major)
        
        assert test_student.student_name  == "John", "Persons name is incorrect"
        assert test_student.student_number  == 1712510105, "Persons number is incorrect"
        assert test_student.student_gender  == "Male", "Gender is incorrect"
        assert test_student.student_nationality  == "China", "Country is incorrect"
        assert test_student.student_phone_number  == [13071838053], "Number is incorrect"
        assert test_student.student_major  == test_major, "Major is incorrect"
        assert test_student.id_type  == "Passport", "Passport is incorrect"
        assert test_student.origin_country  == "China", "Country is incorrect"
        assert test_student.place_of_birth  == "Harare", "City is incorrect"
        
        test_cpm = model.createCoursesPerMajor(test_major=test_major,test_course=test_course)
        
        assert test_cpm.major_cpm == Majors.objects().first(),"Major is incorrect"
        assert test_cpm.module == 1,"module is incorrect"
        assert test_cpm.elective == False,"elective is incorrect"
        assert test_cpm.course_cpm == test_course ,"course is incorrect"
        
        ll=test_student
        test_st = model.createStudentTakes(ts=ll,test_course=test_course,test_semester=test_semester)
        
        assert test_st.student_taking == test_student,"student is incorrect"
        assert test_st.year == 2020,"year is incorrect"
        assert test_st.course_taken == Courses.objects().first(),"course is incorrect"
        assert test_st.semester_taken == Semesters.objects().first(),"Semesters is incorrect"
        
        test_graded = model.createGrading(test_st,test_major)
        
        assert test_graded.student_took == StudentTakes.objects().first() , "Student is incorrect"
        assert test_graded.grade == "A", "Grade is incorrect"
        assert test_graded.attempts == 1, "attempts is incorrect"
        assert test_graded.score == 99.9, "Score is incorrect"
        assert test_graded.credits_ == 4, "Credits is incorrect"
        
        test_schedule = model.creatingSchedule(test_build = test_building,test_seme=test_semester,test_maj=test_major,test_cos=test_course)
        
        assert test_schedule.scheduled_building == Building.objects().first(), "Building is incorrect"
        assert test_schedule.scheduled_year == 2020, "Year is incorrect"
        assert test_schedule.scheduled_semester == Semesters.objects().first(), "Semester is incorrect"
        assert test_schedule.scheduled_major == Majors.objects().first(), "Major is incorrect"
        assert test_schedule.scheduled_course == Courses.objects().first(), "Course is incorrect"
        
        test_note = model.createNotifications(fac = test_faculty,dept = test_dept)
        
        assert test_note.notification == "Hi sexy", "Year is incorrect"
        assert test_note.type_ == "Emergency", "Rank is incorrect"
        assert test_note.responible_faculty == Faculty.objects.first(), "Faculty is incorrect"
        assert test_note.registered_department == Departments.objects.first(), "Department is incorrect"
        
        test_teach = model.createTeaches(fac = test_faculty,sch=test_schedule)
        assert test_teach.teacher == Faculty.objects().first(), "Faculty is wrong"
        assert test_teach.teacher_schedule == SemesterSchedule.objects().first() , "Schedule is wrong"
        
        assert test_teach.class_of_students == [], gg