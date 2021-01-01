"""
Constants module contains several classes each containing constants related to a specific task. The classes contained within Constants are:
    DatabaseConstants : DatabaseConstants contains all of the string contants that will be used to reference the current database in use and its related information
    ModelConstants : ModelConstants contain the constants used for schema like constraints and other document functions
"""
class DatabaseConstants:
    """
    DatabaseConstants contains all of the string contants that will be used to reference the current database in use and its related information
    
    Constants
    ----------
    db_Name : String
        References that name of the database in use
    host : Address
        References the IP address of the database that is in use
    port : Long
        References the port the database is using for its operations
    """
    def __init__(self):
        self.db_Name = "sfdsms"
        self.host = "127.0.0.1"
        self.port = 27017

class FakeDataBaseConstants:
    """
    FakeDataBaseConstants contains the constants to connect to the fake database for mongomock
    
    Constants
    ----------
    db_Name : String
        References that name of the database in use
    host : Address
        References the IP address of the database that is in use
    
    alias : String
        References the other name to identify the database 
    """
    def __init__(self):
        self.alias = "testdb"
        self.host = 'mongomock://localhost'
        self.db_Name = 'mongoenginetest'
        
class ModelConstants:
    """
    ModelConstants : ModelConstants contain the constants used for schema like constraints and other document functions
    Constants
    ----------
    campuses : Tuple of Character String
        Tuple of the campuses avaible to the school
    buildings : Tuple of Character String
        Tuple of the buildings that the school has
    rooms : Tuple of Integers
        Tuple of the all the room numbers avaible. For the sake of the prototype each floor will have 50 floors and there will be a total of 5 floors. This is subject to change for deployment
    semesters : Tuple of Character String
        Tuple of the semesters the school offers
    semester_number : Tuple of Integers
        Tuple of numbers used to identify each semester
    genders : Tuple of Character String
        Tuple of the genders permisable to be identified with by the school
    nationalities : Tuple of Character String
        Tuple of the nationalities permited. For the prototype the only permited nationality will be China 
    modules : Tuple of Integers
        Tuple of the modules the schoo offers
    grades : Tuple of Character String
        Tuple of the grading that the scores can be identified with
    years : Tuple of Integers
        Turple of the permisable years a client can enter into the database
    type_ : Tuple of Strings
        Turple of the permisable emergencies
    submission_type : Tuple of Strings
        Turple containing all the submission types
    max : Long
        Maximum upload size
    """
    def __init__(self):
        self.campuses = ("Jinshagang","Downtown", "Heaven")
        self.buildings = ("A","B","C","MET","D","E","SCIE","CIE","Dawkins")
        self.rooms = tuple(sorted([ i + j for j in range(1,51,1) for i in range(100,600,100)]))
        self.semesters = ("Summer", "Winter","Fall")
        self.semester_number = (1,2,3)
        self.id_type = ("Passport","ID Card")
        self.genders = ("Male","Female","Other")
        self.nationalities = ("China","Zimbabwe")
        self.modules = (1,2,3,4)
        self.grades = ("A","B","C","D","E","F")
        self.years = tuple(sorted([j for j in range(2000,2100,1)]))
        self.type_ = ("Emergency","Warning")
        self.submission_type = ("Resources","Assignments","Submissions")
        self.max = 104857600