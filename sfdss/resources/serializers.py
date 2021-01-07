from rest_framework_mongoengine import serializers
from resources.models import Campus,Semesters,Courses,Departments,Building,Majors,Faculty,Students,CoursesPerMajor,StudentTakes,SemesterSchedule,Notifications,Uploads,SemesterScores,Teaches

class CampusSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Campus
        fields = '__all__'

class SemestersSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Semesters
        fields = '__all__'
    
class CoursesSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Courses
        fields = '__all__'

class DepartmentsSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Departments
        fields = '__all__'

class BuildingSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Building
        fields = '__all__'

class MajorsSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Majors
        fields = '__all__'
        
class FacultySerializer(serializers.DocumentSerializer):
    class Meta:
        depth = 2
        model = Faculty
        fields = ['person_name','person_number','gender','nationality','phone_number','faculty_major']
        
class StudentsSerializer(serializers.DocumentSerializer):
    class Meta:
        depth = 2
        model = Students
        fields = '__all__'
    
class CoursesPerMajorSerializer(serializers.DocumentSerializer):
    class Meta:
        model = CoursesPerMajor
        fields = '__all__'
        
class StudentTakesSerializer(serializers.DocumentSerializer):
    class Meta:
        depth = 2
        model = StudentTakes
        fields = ['student_taking','year_semester','course_taken','semester_taken']
        
class SemesterScoresSerializer(serializers.DocumentSerializer):
    class Meta:
        depth = 2
        model = SemesterScores
        fields = '__all__'
        
class SemesterScheduleSerializer(serializers.DocumentSerializer):
    class Meta:
        model = SemesterSchedule
        fields = '__all__'
        
class NotificationsSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Notifications
        fields = '__all__'

class UploadsSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Uploads
        fields = '__all__'
    
class TeachesSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Teaches
        fields = '__all__'
