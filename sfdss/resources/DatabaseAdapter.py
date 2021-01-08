from resources.models import Uploads, Campus,Semesters,Courses,Departments,Building,Majors,Faculty,Students,CoursesPerMajor,StudentTakes,SemesterScores,SemesterSchedule,Notifications,Teaches
from resources.Constants import ModelConstants
from mongoengine.errors import DoesNotExist
from datetime import datetime
import mimetypes

time = datetime.utcnow()

"""
Module containing the classes necessary to input and retrieve data from the database for the api to work
Classes
----------
DatabaseAdapter
    Contains the functions to input and retrieve data from the database
"""
constants = ModelConstants()
class DatabaseAdapter:
    """
    Contains the functions to input and retrieve data from the database
    
    Functions
    ----------
    writeUpload(file : FILE,member : Faculty) writes the file uploads and relevant information into the database Uploads model
    createLocationTuple(member : Teaches,sub_type :Integer) will be used to generate a string name for the location of the file the user will upload
    createCampus(campus_name : String) takes the string name of a campus and inputs it into the database
    getCampus(campus_name : String) used to find a campus from the database
    
    """
    
    def __init__(self):
        pass
    
    def createCampus(self,campus_name):
        """
        
        createCampus(campus_name : String) takes the string name of a campus and inputs it into the database
        
        Parameters
        ----------
        campus_name : String
            Name of the campus student and faculty belong to

        Returns
        -------
        bool
            True if the input was successful and false if the input was unsuccessful.

        """
        try:
            campus = Campus(campus = campus_name )
            campus.save()
        except:
            return False,"Input was unsuccesful"
        
        return True,"Input was Successful"
    
    def getCampus(self,campus_name):
        """
        getCampus(campus_name : String) used to find a campus from the database

        Parameters
        ----------
        campus_name : String
            String that will be used to identify the record in the database.

        Returns
        -------
        Tuple
            If the record is found then it will return true along with the record but if it is not found the system will return false.

        """
        try:
            campus = Campus.objects.get(campus=campus_name)
        except DoesNotExist:
            return (False,"Record doesn't exist")
        
        return (True, "Record was found" , campus)
    
    def createSemester(self,semester_name,semester_number):
        """
        createSemester(semester_name : String,semester_number : Integer)

        Parameters
        ----------
        semester_name : String
            Name of the semester
        semester_number : Integer
            Number that will be used to identify a semester

        Returns
        -------
        Tuple
            Tuple with boolean and String. If operation worked then it will return true but false otherwise

        """
        try:
            semester = Semesters(semester_name = semester_name, semester_number=semester_number)
            semester.save()
        except:
            return (False,"Input was unsuccesful")
        
        return (True,"Input was Successful")
    
    def getSemester(self,semester_name):
        """
        

        Parameters
        ----------
        semester_name : String
            Name identifying a particular semester.

        Returns
        -------
        Tuple
            If record is available the sytem will send back true and the document otherwise it will return false

        """
        
        try:
            semester = Semesters.objects.get(semester_name=semester_name)
            
        except DoesNotExist:
            return (False,"Record doesn't exist")
        
        return (True, "Record was found" , semester)
    
    def createCourse(self,course_name,course_number):
        """
        createCourse(course_name : String,course_number : Integer)

        Parameters
        ----------
        course_name : String
            Name of the course
        course_number : Integer
            Number that will be used to identify a course

        Returns
        -------
        Tuple
            Tuple with boolean and String. If operation worked then it will return true but false otherwise

        """
        try:
            course = Courses(course_name = course_name, course_id=course_number)
            course.save()
        except:
            return (False,"Input was unsuccesful")
        
        return (True,"Input was Successful")
    
    def getCourse(self,course_id):
        """
        

        Parameters
        ----------
        course_id : Integer
            Number identifying the course in the collection

        Returns
        -------
        Tuple
            If record is available the sytem will send back true and the document otherwise it will return false

        """
        
        try:
            course = Courses.objects.get(course_id=course_id)
            
        except DoesNotExist:
            return (False,"Record doesn't exist")
        
        return (True, "Record was found" , course)
    
    def createDepartment(self,dept):
        """
        
        createDepartment(dept : String) takes the string name of a department and inputs it into the database
        
        Parameters
        ----------
        dept : String
            Name of the department

        Returns
        -------
        bool
            True if the input was successful and false if the input was unsuccessful.

        """
        try:
            dpt = Departments(department_name = dept )
            dpt.save()
        except:
            return False,"Input was unsuccesful"
        
        return True,"Input was Successful"
    
    def getDepartment(self,dept):
        """
        getDepartment(dept : String) used to find a department from the database

        Parameters
        ----------
        dept : String
            String that will be used to identify the record in the database.

        Returns
        -------
        Tuple
            If the record is found then it will return true along with the record but if it is not found the system will return false.

        """
        try:
            dpt = Departments.objects.get(department_name=dept)
        except DoesNotExist:
            return (False,"Record doesn't exist")
        
        return (True, "Record was found" , dpt)
    
    def createBuilding(self,campus, building_name, room =101):
        """
        createBuilding(campus : Campus, building_name : String, room : Integer) creates a building in the database

        Parameters
        ----------
        campus : Campus
            Campus in which the building belongs to
        building_name : String
            Name of the building
        room : Integer
            The room the building has

        Returns
        -------
        Tuple
            If the record is found then it will return true along with the record but if it is not found the system will return false.

        """
        try:
            build = Building(building_campus = campus,building=building_name,room_number =room)
            build.save()
        except:
            return (False,"Input was unsuccesful")
        
        return (True,"Input was Successful")
    
    def getBuilding(self,building,room =101):
        """
        getBuilding(building : String) used to find a building from the database

        Parameters
        ----------
        building : String
            String that will be used to identify the record in the database.
        room : Integer
            Integer used to identifying a specific room building
        Returns
        -------
        Tuple
            If the record is found then it will return true along with the record but if it is not found the system will return false.

        """
        try:
            build = Building.objects.get(building=building,room_number=room)
        except DoesNotExist:
            return (False,"Record doesn't exist")
        
        return (True, "Record was found" , build)
    
    def createMajors(self,dept, major_name):
        """
        createMajors(dept : Departments, major_name : String) is a creation 

        Parameters
        ----------
        dept : Departments
            The department in which the major belongs to
            
        major_name : String
            The name of major

        Returns
        -------
        Tuple
            If the record is found then it will return true along with the record but if it is not found the system will return false.

        """
        try:
            majer = Majors(major_department = dept,major=major_name)
            majer.save()
        except:
            return (False,"Input was unsuccesful")
        
        return (True,"Input was Successful")
    
    def getMajors(self,major):
        """
        getMajors(self,major : String) String to identify a specific major

        Parameters
        ----------
        major : String
            String to identify a document

        Returns
        -------
        Tuple
            If the record is found then it will return true along with the record but if it is not found the system will return false.


        """
        try:
            majer = Majors.objects.get(major=major)
        except DoesNotExist:
            return (False,"Record doesn't exist")
        
        return (True, "Record was found" , majer)
    def createFaculty(self,name, number,major,gender= "Male",nationality="China",phone = [12345678,12345678]):
        """
        
        createFaculty(name : String, number : Integer,gender : String,nationality : String,phone : List of Integer,major : Majors) used to create a new teacher 
        Parameters
        ----------
        name : String
            The name of the faculty member
            
        number : Integer
            The number used as an identification
            
        gender : String, optional
            Gender a teacher identifies themselves with. The default is "Male".
            
        nationality : String, optional
            Place the teacher comes from. The default is "China".
            
        phone : Integer List, optional
            Number used to identify the teacher. The default is [12345678,12345678].
            
        major : Majors
            Major the teacher belongs to.

        Returns
        -------
        Tuple
            If the record is found then it will return true along with the record but if it is not found the system will return false.


        """
        try:
            faculty = Faculty(person_name = name,person_number=number,gender =gender,nationality=nationality,phone_number=phone,faculty_major=major)
            faculty.save()
        except:
            return (False,"Input was unsuccesful")
        
        return (True,"Input was Successful")
    
    def getFaculty(self,number):
        """
        getFaculty(number : Integer) used to return the record 

        Parameters
        ----------
        number : Integer
            Number used to identify a record

        Returns
        -------
        Tuple
            If the record is found then it will return true along with the record but if it is not found the system will return false.


        """
        try:
            fac = Faculty.objects.get(person_number=number)
        except DoesNotExist:
            return (False,"Record doesn't exist")
        
        return (True, "Record was found" , fac)
    
    def createStudent(self,name, number,major,origin="China",place_of_birth= "Home",_id = "Passport" ,gender= "Male",nationality="China",phone = [12345678,12345678]):
        """
        createStudent(name : String, number : Integer,major : Majors,origin : String,place_of_birth : String,_id : String ,gender : String,nationality : String,phone : Integer List) creates a new student in the database

        Parameters
        ----------
        name : String
            The name of the student.
            
        number : Integer
            Integer identifying the student.
            
        major : Majors
            Major the student belongs to.
            
        origin : String, optional
            Country the student comes from. The default is "China".
            
        place_of_birth : String, optional
            City or province the student was born in. The default is "Home".
            
        _id : String, optional
            The identification the student is using. The default is "Passport".
            
        gender : String, optional
            The gender the student is using. The default is "Male".
            
        nationality : String, optional
            The country from which is student was born. The default is "China".
            
        phone : List of Integers, optional
            The phone numbers the student uses. The default is [12345678,12345678].

        Returns
        -------
        Tuple
            If the record is found then it will return true along with the record but if it is not found the system will return false.

        """
        try:
            student = Students(student_name = name,student_number=number,student_gender =gender,student_nationality=nationality,student_phone_number=phone,student_major=major,id_type=_id,enrollment_date=time,origin_country=origin,place_of_birth=place_of_birth)
            student.save()
        except:
            return (False,"Input was unsuccesful")
        
        return (True,"Input was Successful")
    
    def getStudent(self,number):
        """
        getStudent(number : Integer) used to return the record 

        Parameters
        ----------
        number : Integer
            Number used to identify a record

        Returns
        -------
        Tuple
            If the record is found then it will return true along with the record but if it is not found the system will return false.


        """
        try:
            stu = Students.objects.get(student_number=number)
        except DoesNotExist:
            return (False,"Record doesn't exist")
        
        return (True, "Record was found" , stu)
    
    def createStudentTakes(self,student,year,course,semester):
        """
        

        Parameters
        ----------
        student : Students
            DESCRIPTION.
        year : DateTime
            DESCRIPTION.
        course : Courses
            DESCRIPTION.
        semester : Semesters
            DESCRIPTION.

        Returns
        -------
        bool
            DESCRIPTION.
        str
            DESCRIPTION.

        """
        try:
            student_takes = StudentTakes(student_taking=student,year_semester=year,course_taken=course,semester_taken=semester)
            student_takes.save()
        except:
            return (False,"Input was unsuccesful")
        return (True,"Input was Successful")
    
    
    def getStudentTakes(self,student_id):
        """
        

        Parameters
        ----------
        student_id : Long
            DESCRIPTION.

        Returns
        -------
        TYPE
            DESCRIPTION.

        """
        try:
            student=self.getStudent(student_id)
            stu = StudentTakes.objects(student_taking=student[2]).all()
        except DoesNotExist:
            return (False,"Record doesn't exist")
        
        return (True, "Record was found" , stu)
    
    def createSemesterScores(self,studentTaking,grade='A',attemps = 1,score = 99,credit = 4):
        '''
        

        Parameters
        ----------
        studentTaking : StudentTakes
            DESCRIPTION.
        grade : String, optional
            DESCRIPTION. The default is 'A'.
        attemps : Integer, optional
            DESCRIPTION. The default is 1.
        score : Float, optional
            DESCRIPTION. The default is 99.
        credit : Integer, optional
            DESCRIPTION. The default is 4.

        Returns
        -------
        bool
            DESCRIPTION.
        str
            DESCRIPTION.

        '''
        try:
            student_got = SemesterScores(student_took =studentTaking ,grade =grade,attempts =attemps,score =score,credits_ =credit)
            student_got.save()
        except:
            return (False,"Input was unsuccesful")
        return (True,"Input was Successful")
        
            
        return (True,"Input was Successful")
    
    def getSemesterScores(self,student_number):
        """
        

        Parameters
        ----------
        student_number : Long
            DESCRIPTION.

        Returns
        -------
        TYPE
            DESCRIPTION.

        """
        try:
            
            student_tooketh = self.getStudentTakes(student_number)
            queryset = student_tooketh[2]
            
            stu = [SemesterScores.objects.get(student_took=item) for item in queryset]
        except DoesNotExist:
            return (False,"Record doesn't exist",{})
        
        return (True, "Record was found" , stu)
    
    def createCPM(self,semester,major,course,year=2020,mod=1,elective=False):
        """
        

        Parameters
        ----------
        major : Majors
            DESCRIPTION.
        course : Courses
            DESCRIPTION.
        mod : Integer, optional
            DESCRIPTION. The default is 1.
        elective : Boolean, optional
            DESCRIPTION. The default is False.

        Returns
        -------
        bool
            DESCRIPTION.
        str
            DESCRIPTION.

        """
        

        
        try:
            cpm = CoursesPerMajor(major_cpm=major,module=mod,elective=elective,course_cpm=course,year_course=year,semester_course=semester)
            cpm.save()
        except:
            return (False,"Input was unsuccesful")
        return (True,"Input was Successful")

    def getCPM(self,major):
        """
        

        Parameters
        ----------
        major : Majors
            DESCRIPTION.

        Returns
        -------
        bool
            DESCRIPTION.
        str
            DESCRIPTION.
        TYPE
            DESCRIPTION.

        """
        try:
            
            major_set = self.getMajors(major.major)
            query = major_set[2]
            stu = CoursesPerMajor.objects(major_cpm=query)
        except DoesNotExist:
            return (False,"Record doesn't exist",{})
        
        return (True, "Record was found" , stu)
        
    def dropCollections(self):
        """
        dropCollections() deletes all the collections stored in the database

        Returns
        -------
        None.

        """
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
        StudentTakes.drop_collection()
        SemesterScores.drop_collection()
        CoursesPerMajor.drop_collection()
    
    def getCPMByID(self,student_id):
        '''
        

        Parameters
        ----------
        student_id : Integer
            DESCRIPTION.

        Returns
        -------
        bool
            DESCRIPTION.
        str
            DESCRIPTION.
        TYPE
            DESCRIPTION.

        '''
        try:
            
            sTuple = self.getStudent(student_id)
            student = sTuple[2]
            maj = Majors.objects.get(major=student.student_major.major)
            stu = self.getCPM(maj)
        except DoesNotExist:
            return (False,"Record doesn't exist",{})
        
        return stu
    def dummyInnitialize(self):
        """
        dummyInnitialize() generates fake database records for prototype testing 

        Returns
        -------
        Boolean 
            if anything is missing then false is sent with a warning of where the error occurred otherwise it will say True and send back message

        """
        Campases = ["Jinshagang", "Downtown", "Heaven"]
        Semasters = {"Winter" : 1,"Fall" : 3,"Summer" : 2}
        Coursas = {"Intro To Comp Sci" : 2323,"Intro to Economics" : 2424,"CAD" : 2525}
        Dapartment = ["SCIE", "SAH", "SE"]
        Buildang = ["A" ,"B" ,"C" ]
        MajeEr = ["Computer Science" , "Philosophy", "Accounting"]
        Facaty = [["Mr Wang", 9725001001 ],["Mr Edwards", 9725001002],["Mr Henry", 9725001003]]
        Studs = [["Bob", 1712510101],["Doe", 1712510103],["Albert", 1712510102]]
        
        
        for campus in Campases:
            self.createCampus(campus)
        
        for key in Semasters:
            self.createSemester(semester_name = str(key),semester_number = Semasters[key])
        
        for key in Coursas:
            self.createCourse(course_name = str(key),course_number = Coursas[key])
        
        for dept in Dapartment:
            self.createDepartment(dept)
        
        for number in range(3):
            camp = self.getCampus(Campases[number])
            self.createBuilding(campus=camp[2],building_name=Buildang[number])
            
        for number in range(3):
            dept = self.getDepartment(Dapartment[number])
            self.createMajors(dept=dept[2],major_name=MajeEr[number])
            
        
        counter = 0
        check = False
        
        for item in Facaty:
            maj = self.getMajors(MajeEr[counter])
            self.createFaculty(name= item[0],number=item[1],major=maj[2])
            
            counter = counter + 1
            
        counter = 0
        for item in Studs:
            maja = self.getMajors(MajeEr[counter])
            self.createStudent(name= item[0],number=item[1],major=maja[2])
            if check == False:
                check = True
                continue
            counter = counter + 1
        
        counter = 0
        seme = Semesters.objects.first()
        maj = Majors.objects.first()
        for item in range(3):
            ckeys = list(Coursas.values())
            cos_id = ckeys[item]
            cTuple= self.getCourse(cos_id)
            cos = cTuple[2]
            self.createCPM(major=maj,course=cos,mod=item+1,semester=seme)
            
        for item in range(3):
            ss = self.getStudent(Studs[counter][1])
            student = ss[2]
            cc =list(Coursas.values())
            ccc = cc[counter]
            cccc = self.getCourse(ccc)
            cos = cccc[2]
            ss =list(Semasters.keys())
            sss = ss[counter]
            ssss = self.getSemester(sss)
            seme = ssss[2]
          
            self.createStudentTakes(student=student,year=2020,course=cos,semester=seme)
            
            counter = counter + 1
            
        takes = StudentTakes.objects.all()
        for items in takes:
            self.createSemesterScores(studentTaking=items)
        
        
        if Campus.objects.count() != 3:
            return (False, "Campus count is wrong!" + str(Campus.objects.count()))
        
        if Semesters.objects.count() != 3:
            return (False, "Semester count is wrong!" + str(Semesters.objects.count()))
        
        if Courses.objects.count() != 3:
            return (False, "Courses count is wrong!" + str(Courses.objects.count()))
        
        if Departments.objects.count() != 3:
            return(False, "Departments count is wrong!" + str(Departments.objects.count()))
        
        if Building.objects.count() != 3:
            return (False, "Building count is wrong!" + str(Building.objects.count()))
        
        if Majors.objects.count() != 3:
            return (False, "Majors count is wrong!" + str(Majors.objects.count()))
        
        if Faculty.objects.count() != 3:
            return (False, "Faculty count is wrong!" + str(Faculty.objects.count()))
        
        if Students.objects.count() != 3:
            return (False, "Students count is wrong!" + str(Students.objects.count()))
        if StudentTakes.objects.count() != 3:
            return (False, "Students taking count is wrong!" + str(Students.objects.count()))
        
        if SemesterScores.objects.count() != 3:
            return (False, "Semester Scores taking count is wrong!" + str(Students.objects.count()))
        
        if CoursesPerMajor.objects.count() != 3:
            return (False, "Course per major taking count is wrong!" + str(Students.objects.count()))
        return (True, "Done!")
        
    def writeUpload(self,file,member,file_name,sub_type = 1):
        """
        def writeUpload(file : FIL,member : Faculty) writes the file uploads and relevant information into the database Uploads model

        Parameters
        ----------
        file : FILE
            File that will be uploaded to the database
        member : tEACHES
            Teaches document class that will be inputed along the uploaded file to identify the person who uploaded the file and the course to upload under
        file_name : String
            Name of the file used to identify the file in the database
        Returns
        -------
        upload : Uploads
            Return the uploads model of the recently created file

        """
        
        location = self.createLocationTuple(member,sub_type)
        upload = Uploads(file_name=file_name,location = location,uploader=member,upload_time=time)
        upload.file.put(file, content_type = mimetypes.guess_type(file_name)[0])
        upload.save()
        return upload
    
    def createLocationTuple(self,member,sub_type):
        """
        createLocationTuple(member : Teaches,sub_type :Integer) will be used to generate a string name for the location of the file the user will upload

        Parameters
        ----------
        member : Teaches
            Contains a document with the relevant information to create a file location

        Returns
        -------
        location : tuple of strings
            The strings that will be used to identify the file

        """
        dept = str(member.teacher_schedule.scheduled_major.major_department)
        major = str(member.teacher_schedule.scheduled_major.major)
        course = str(member.teacher_schedule.scheduled_course.course_name)
        teach = str(member.teacher.person_name)
        semester = str(member.teacher_schedule.scheduled_semester.semester_name)
        sub_type = str(constants.submission_type[sub_type])
        location = " ".join((dept,major,course,teach,semester,sub_type))
        return location
        