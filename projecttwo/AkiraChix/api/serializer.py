from student.models import Student

from teacher.models import Teacher

from Course.models import Course

from rest_framework import serializers

class StudentSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Student
		fields = "__all__"

class TeacherSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Teacher
		fields = "__all__"		


class CourseSerializer(serializers.ModelSerializer):
	class Meta:
		model = Course
		fields = "__all__"	




























