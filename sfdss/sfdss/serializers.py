from rest_framework_mongoengine import serializers
from sfdss.models import Campus,Semesters,Courses,Departments,Building,Majors,Faculty,Students,CoursesPerMajor,StudentTakes,SemesterSchedule,Notifications,Uploads,SemesterScores

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
        model = Faculty
        fields = '__all__'
        
class StudentsSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Students
        fields = '__all__'
    
class CoursesPerMajorSerializer(serializers.DocumentSerializer):
    class Meta:
        model = CoursesPerMajor
        fields = '__all__'
        
class StudentTakesSerializer(serializers.DocumentSerializer):
    class Meta:
        model = StudentTakes
        fields = '__all__'
        
class SemesterScoresSerializer(serializers.DocumentSerializer):
    class Meta:
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
        
