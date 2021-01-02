from mongoengine import  Document, StringField,IntField,ReferenceField,LongField,DateTimeField,ListField,BooleanField,FloatField,FileField,CASCADE,DO_NOTHING
from resources.Constants import ModelConstants
constants = ModelConstants()

"""
models module contains the schema like design of how mongodb will store data as well as how it operates on it.the database models are:
    Building : Contains information about the building venues for courses
    Semesters : Contains information about semesters
    Departments : Contains information related to departments
    Majors : Contains information relevant to the majors the school offers
    Courses : Contains information about the courses offered by the school
    Students : Contains information about all the students in the school
    CoursesPerMajor : Contains the courses contained in each major and relavant information about courses in the major
    StudentTakes : Contains the information to do with which student take what course
    SemesterScores : Contains the scores a student got in each semester
    SemesterSchedule : Contains the planned schedule for courses
    Notifications : Contain the notifications sent through the school channel
    Faculty : Contains information about the teaching faculty at the school
    Uploads : Contains informaiton about file that have been uploaded by the user
    Campus : Contains campuses and their information
    Teaches : Contains informaiton about the teaching schedule of teachers
"""



class Campus(Document):
    """
    Campus : Contains campus and their information\n
    Fields
    ----------
    campus_name : Character String
        The name of campus\n
    """
    campus = StringField(required = True,unique = True, choices = constants.campuses )
    meta={'indexes' : ['campus','$campus']}
    
class Semesters(Document):
    """
    Semesters : Contains information about semesters\n
    Fields
    ----------
    semester_name : Character String
        Name of the semester\n
    semester_number : Integer
        Number of correlating to the semester\n
    """
    semester_number = IntField(required = True, unique=True,choices = constants.semester_number )
    semester_name = StringField(required = True,unique=True, choices = constants.semesters )
    meta={'indexes' : ['semester_name','$semester_name']}

class Courses(Document):
    """
    Courses : Contains information about the courses offered by the school\n
    Fields
    ----------
    course_name : Character String
        Name of the course\n
    course_id : Long
        Identifying id for the course\n
    """
    course_name = StringField(required = True,unique = True)
    course_id = LongField(required = True,unique=True)
    meta={'indexes' : ['course_name','$course_name',('course_name','+course_id'),'course_id'],'ordering' : ['+course_id']}

class Departments(Document):
    """
    Departments : Contains information related to departments
    
    Fields
    ----------
    department_name : Character String
        Name of the department
        
    """
    department_name = StringField(required = True,unique=True)
    meta={'indexes' : ['department_name','$department_name']}
    
class Building(Document):
    """
    Building : Contains information about the building venues for courses
    
    Fields
    ----------
    building : Character String
        Building name
        
    building_campus : Document
        The name of the campus the building belongs to
        
    room_number : Integer
        The room number of the course
        
    """
    building_campus = ReferenceField(Campus,reverse_delete_rule=CASCADE,required = True)
    building = StringField(required = True,unique_with=['building_campus'],choices = constants.buildings)
    room_number = IntField(required = True,unique_with=['building'], choices = constants.rooms )
    meta={'indexes' : [('building','+room_number')]}
    

class Majors(Document):
    """
    Majors : Contains information relevant to the majors the school offers
    
    Fields
    ----------
    major_department : Document
        references the departments document and thus its information
        
    major : Character String
        name of the major
        
    """
    major_department = ReferenceField(Departments,required = True,reverse_delete_rule=DO_NOTHING)
    major = StringField(required = True,unique=True)
    
class Faculty(Document):
    """
    Faculty : Contains information about the teaching faculty at the school
    
    Fields
    ----------
    person_name : Character String
        Name of the person
        
    person_number : Long
        Identifying id for the person
        
    gender : Character String
        Identifying the legal gender of the person
        
    nationality : Character String
        Country which issued the identification the person is using to enroll into the school
        
    phone_number : List of Long
        Contains a list of the phone numbers which can be used to contact the person
        
    faculty_major : Character String
        The major the person belongs to
        
    """
    person_name = StringField(required = True)
    person_number = LongField(required = True,unique=True)
    gender = StringField(required = True, choices = constants.genders )
    nationality = StringField(required = True, choices = constants.nationalities )
    phone_number = ListField(LongField(),default=list)
    faculty_major = ReferenceField(Majors,required = True,reverse_delete_rule=DO_NOTHING)
    
    meta = {'indexes' : ['person_number']}
    
class Students(Document):
    """
    Students : Contains information about all the students in the school
    Fields
    ----------
    student_name : Character String
        Name of the person
        
    student_number : Long
        Identifying id for the person
        
    student_gender : Character String
        Identifying the legal gender of the person
        
    student_nationality : Character String
        Country which issued the identification the person is using to enroll into the school
        
    student_phone_number : List of Long
        Contains a list of the phone numbers which can be used to contact the person
        
    student_major : Character String
        The major the person belongs to
        
    id_type : Character String
        The type of the form used to identify the student
        
    enrollment_date : Datetime
        The date the student enrolled in the school
        
    origin_country : Character String
        The country from which the student was born in
        
    place_of_birth : Character String
        The city or province the student was born in
        
    """
    student_name = StringField(required = True)
    student_number = LongField(required = True,unique=True)
    student_gender = StringField(required = True, choices = constants.genders )
    student_nationality = StringField(required = True, choices = constants.nationalities )
    student_phone_number = ListField(LongField(),default=list)
    student_major = ReferenceField(Majors,required = True,reverse_delete_rule=DO_NOTHING)
    id_type = StringField(required = True,choices=constants.id_type)
    enrollment_date = DateTimeField(required = True)
    origin_country = StringField(required = True,choices=constants.nationalities)
    place_of_birth = StringField(required = True)
    meta = {'indexes' : ['student_number']}
    
class CoursesPerMajor(Document):
    """
    CoursesPerMajor : Contains the courses contained in each major and relavant information about courses in the major
    Fields
    ----------
    major_cpm : Document
        Major of the corresponding course 
    module : Integer
        Module the corresponging course belongs to in its major
    elective : Boolean
        Whether or not the course is elective
    course_cpm : Document
        The course name and details
    """
    
    major_cpm = ReferenceField(Majors,required = True,reverse_delete_rule=CASCADE)
    module = IntField(required = True,unique_with=['major_cpm'], choices = constants.modules)
    elective = BooleanField(default=False)
    course_cpm = ReferenceField(Courses,required = True,unique_with=['major_cpm','module'],reverse_delete_rule=CASCADE)

    
class StudentTakes(Document):
    """
    StudentTakes : Contains the information to do with which student takes what course
    Fields
    ----------
    student_taking : Document
        References the student taking the corresponding course
    course_taken : Document
        References the course being taken by the student
    year : Integer 
        Year the student will be taking a particular year
    semester_taken : Document
        References the semester in which the student took the course 
    """
    student_taking = ReferenceField('Students',required = True,reverse_delete_rule=DO_NOTHING)
    year = IntField(required = True,choices=constants.years)
    course_taken = ReferenceField(Courses,required = True)
    semester_taken = ReferenceField(Semesters,required = True)
    
    
class SemesterScores(Document):
    """
    SemesterScores : Contains the scores a student got in each semester
    Fields
    ----------
    student_took : Document
        Student information for the one who took the exam and when he took the course
    year : Integer
        Year in which the student took the course
    semester : Document
        References the semester the student has taken
    course : Document
        Course information for the corresponding results
    grade : Character String
        Grade the student recieved for completing the course
    attempts : Integer
        Number of attempts the student made to get the score he finally recieved
    score : Double
        Score the student was award upon completing the course
    credits : Integer
        Credit the student was awarded upong completing the course
    major_exam : Document
        Major the course belongs to
    """
    student_took = ReferenceField(StudentTakes,required = True,reverse_delete_rule=DO_NOTHING)
    grade = StringField(required = True, choices = constants.grades)
    attempts = IntField(required = True)
    score = FloatField(required = True)
    credits_ = IntField(required = True)
    
class SemesterSchedule(Document):
    """
    SemesterSchedule : Contains the planned schedule for courses
    Fields
    ----------
    scheduled_course : Document
        References the course that is on the schedule
    scheduled_building : Document
        References the building venue
    scheduled_time : Datatime
        The time in which the course will be taken
    scheduled_year : Integer
        The year the course is to be taken
    scheduled_semester : Document
        References the semester the student has to partake in the course
    scheduled_major : Document
        References the major the student belongs to
    """
    scheduled_building = ReferenceField(Building,required = True,reverse_delete_rule=CASCADE)
    scheduled_year = IntField(required = True,choices = constants.years)
    scheduled_semester = ReferenceField(Semesters,required = True,reverse_delete_rule=CASCADE)
    scheduled_time = DateTimeField(required = True,unique_with=['scheduled_semester','scheduled_year','scheduled_building'])
    scheduled_major = ReferenceField(Majors,required = True,reverse_delete_rule=CASCADE)
    scheduled_course = ReferenceField(Courses,required = True,unique_with=['scheduled_building','scheduled_time','scheduled_year','scheduled_semester'],reverse_delete_rule=CASCADE)
    
class Teaches(Document):
    """
    Teaches : Contains informaiton about the teaching schedule of teachers
    Fields
    ----------
    teacher : Document
        The name of the teacher in charge
    teacher_schedule : Document
        Contains the planned schedule for teacher in a particular course
    """
    teacher = ReferenceField(Faculty,required = True,reverse_delete_rule=CASCADE)
    teacher_schedule = ReferenceField(SemesterSchedule,required = True,unique_with=['teacher'],reverse_delete_rule=CASCADE)
    class_of_students= ListField(ReferenceField(Students),default = list)
    
class Uploads(Document):
    """
    Uploads : Contains informaiton about file that have been uploaded by the user
    Fields
    ----------
    file_name : Character String
        The name of the file
    location : Character String
        The location of the uploaded file
    uploader : Document
        Information about the faculty member who uploaded the file
    time : Datetime
        The time the file was uploaded to the database
    """
    file_name = StringField(required = True,unique=True)
    location = StringField(required = True)
    uploader = ReferenceField(Teaches,required = True,reverse_delete_rule=CASCADE)
    upload_time = DateTimeField(required = True)
    file = FileField(required = True)
    meta={'indexes' : ['file_name','$file_name','location','$location']}
    
class Notifications(Document):
    """
    Notifications : Contain the notifications sent through the school channel
    Fields
    ----------
    notification : Character String 
        Contains the information about the 
    type : Character String
        Contains the type of notification by its urgency
    note_time : Datetime
        Specifies when the notification was made
    upload : Document
        Contains information about any uploaded file to the server tied to the notification
    registered_department : Document
        References the department that posted the notification
    responible_faculty : Document
        References the faculty person that uploaded the notifications
    """
    notification_name =  StringField(required = True)
    notification = StringField(required = True)
    type_ = StringField(required = True, choices = constants.type_)
    note_time = DateTimeField(required = True)
    upload = ReferenceField(Uploads,required = False ,reverse_delete_rule=CASCADE)
    registered_department = ReferenceField(Departments,required = True,reverse_delete_rule=CASCADE)
    responible_faculty = ReferenceField(Faculty,required = True,reverse_delete_rule=CASCADE)
    targets = ListField(ReferenceField(Students,reverse_delete_rule=CASCADE),default=list)