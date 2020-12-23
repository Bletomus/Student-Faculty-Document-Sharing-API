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
    Departments : Contains information related to departments\n
    Fields
    ----------
    department_name : Character String
        Name of the department\n
    """
    department_name = StringField(required = True,unique=True)
    meta={'indexes' : ['department_name','$department_name']}
    
class Building(Document):
    """
    Building : Contains information about the building venues for courses\n
    Fields
    ----------
    building : Character String
        Building name
    campus : Document
        The name of the campus the building belongs to\n
    room_number : Integer
        The room number of the course\n
    """
    campus = ReferenceField(Campus,reverse_delete_rule=CASCADE,required = True)
    building = StringField(required = True,unique_with=['campus'],choices = constants.buildings)
    room_number = IntField(required = True,unique_with=['building'], choices = constants.rooms )
    meta={'indexes' : [('building','+room_number')]}
    

class Majors(Document):
    """
    Majors : Contains information relevant to the majors the school offers\n
    Fields
    ----------
    department : Document
        references the departments document and thus its information\n
    major : Character String
        name of the major\n
    """
    department = ReferenceField(Departments,required = True,reverse_delete_rule=CASCADE)
    major = StringField(required = True,unique=True)
    
class Faculty(Document):
    """
    Faculty : Contains information about the teaching faculty at the school\n
    Fields
    ----------
    person_name : Character String
        Name of the person\n
    person_number : Long
        Identifying id for the person\n
    gender : Character String
        Identifying the legal gender of the person\n
    nationality : Character String
        Country which issued the identification the person is using to enroll into the school\n
    phone_number : List of Long
        Contains a list of the phone numbers which can be used to contact the person\n
    major : Character String
        The major the person belongs to\n
    """
    person_name = StringField(required = True)
    person_number = LongField(required = True,unique=True)
    gender = StringField(required = True, choices = constants.genders )
    nationality = StringField(required = True, choices = constants.nationalities )
    phone_number = ListField(LongField(),default=list)
    major = ReferenceField(Majors,required = True,reverse_delete_rule=DO_NOTHING)
    
    meta = {'allow_inheritance': True,'indexes' : ['person_number']}
    
class Students(Faculty):
    """
    Students : Contains information about all the students in the school
    Fields
    ----------
    id_type : Character String
        The type of the form used to identify the student
    enrollment_date : Datetime
        The date the student enrolled in the school
    origin_country : Character String
        The country from which the student was born in
    place_of_birth : Character String
        The city or province the student was born in
    """
    id_type = StringField(required = True,choices=constants.id_type)
    enrollment_date = DateTimeField(required = True)
    origin_country = StringField(required = True,choices=constants.nationalities)
    place_of_birth = StringField(required = True)
    
class CoursesPerMajor(Document):
    """
    CoursesPerMajor : Contains the courses contained in each major and relavant information about courses in the major
    Fields
    ----------
    major : Document
        Major of the corresponding course 
    module : Integer
        Module the corresponging course belongs to in its major
    elective : Boolean
        Whether or not the course is elective
    course : Document
        The course name and details
    """
    
    major =  ReferenceField(Majors,required = True,reverse_delete_rule=CASCADE)
    module = IntField(required = True,unique_with=['major'], choices = constants.modules)
    elective = BooleanField(default=False)
    course =  ReferenceField(Courses,required = True,unique_with=['major','module'],reverse_delete_rule=CASCADE)
    

class StudentTakes(Document):
    """
    StudentTakes : Contains the information to do with which student takes what course
    Fields
    ----------
    student : Document
        References the student taking the corresponding course
    course : Document
        References the course being taken by the student
    year : Integer 
        Year the student will be taking a particular year
    semester : Document
        References the semester in which the student took the course 
    """
    student = ReferenceField(Students,required = True,reverse_delete_rule=DO_NOTHING)
    year = IntField(required = True)
    course = ReferenceField(Courses,required = True)
    semester = ReferenceField(Semesters,required = True)
    
class SemesterScores(Document):
    """
    SemesterScores : Contains the scores a student got in each semester
    Fields
    ----------
    student : Document
        Student information for the one who took the exam
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
    major : Document
        Major the course belongs to
    """
    student = ReferenceField(Students,required = True,reverse_delete_rule=DO_NOTHING)
    year = IntField(required = True)
    semester = ReferenceField(Semesters,required = True,reverse_delete_rule=DO_NOTHING)
    course = ReferenceField(Courses,required = True,reverse_delete_rule=DO_NOTHING)
    grade = StringField(required = True, choices = constants.grades)
    attempts = IntField(required = True)
    score = FloatField(required = True)
    credits_ = IntField(required = True)
    major = ReferenceField(Majors,required = True,reverse_delete_rule=DO_NOTHING)
    
class SemesterSchedule(Document):
    """
    SemesterSchedule : Contains the planned schedule for courses
    Fields
    ----------
    course : Document
        References the course that is on the schedule
    building : Document
        References the building venue
    time : Datatime
        The time in which the course will be taken
    year : Integer
        The year the course is to be taken
    semester : Document
        References the semester the student has to partake in the course
    major : Document
        References the major the student belongs to
    """
    building = ReferenceField(Building,required = True,reverse_delete_rule=CASCADE)
    year = IntField(required = True)
    semester = ReferenceField(Semesters,required = True,reverse_delete_rule=CASCADE)
    time = DateTimeField(required = True,unique_with=['semester','year','building'])
    major = ReferenceField(Majors,required = True,reverse_delete_rule=CASCADE)
    course = ReferenceField(Courses,required = True,unique_with=['building','time','year','semester'],reverse_delete_rule=CASCADE)
    

    
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
    uploader = ReferenceField(Faculty,required = True,reverse_delete_rule=DO_NOTHING)
    time = DateTimeField(required = True)
    file = FileField(required = True)
    meta={'indexes' : ['file_name','$file_name','location','$location']}
    
class Notifications(Document):
    """
    Notifications : Contain the notifications sent through the school channel
    Fields
    ----------
    notifications : Character String 
        Contains the information about the 
    type : Character String
        Contains the type of notification by its urgency
    time : Datetime
        Specifies when the notification was made
    upload : Document
        Contains information about any uploaded file to the server tied to the notification
    department : Document
        References the department that posted the notification
    faculty : Document
        References the faculty person that uploaded the notifications
    """
    notifications = StringField(required = True)
    type_ = StringField(required = True)
    time = DateTimeField(required = True)
    upload = ReferenceField(Uploads,required = True,reverse_delete_rule=CASCADE)
    department = ReferenceField(Departments,required = True,reverse_delete_rule=CASCADE)
    faculty = ReferenceField(Faculty,required = True,reverse_delete_rule=CASCADE)
    meta={'ordering' : '-time'}