from django.test import TestCase
from teacher.models import Teacher
from course.models import Course
import datetime



class  TeacherCourseTestCase(TestCase):
	def setUp(self):
		self.teacher_a = Teacher.objects.create(
			first_name = "Mary",
			last_name = "Njeri",
			date_of_birth = datetime.date(1998,7,25),
			gender = "female",
			registration_number = "2017",
			email =" marynjeri@gmail.com",
			phone_number = "+254717899760",
			date_joined = datetime.date.today(),



			)

		self.teacher_a = Teacher.objects.create(
		first_name = "Catherine",
		last_name ="Wanjiru",
		date_of_birth = datetime.date(1997,6,20),
		gender = "female",
		registration_number = "2019",
		email = "watiricate16@gmail.com",
		phone_number = "+25404660035",
		date_joined = datetime.date.today(),
		)


		self.teacher_b = Teacher.objects.create(
			first_name = "Clarence",
			last_name ="Anyango",
			date_of_birth = datetime.date(1992,10,16),
			gender = "male",
			registration_number = "2012",
			email = "clarean@gmail.com",
			phone_number = "+2543678235",
			date_joined = datetime.date.today(),

		)

		self.python = Course.objects.create(
			name = "Python",
			duration_in_months = 9,
			start_date = datetime.date(2019,2,2),
			end_date = datetime.date(2019,11,30),
			description = "Backend programming language",
		)
		self.javascript = Course.objects.create(
			name = "Javascript",
			duration_in_months = 9,
			start_date = datetime.date(2019,2,2),
			end_date = datetime.date(2019,11,30),
			description = "Frontend stuff",
		)

		self.design = Course.objects.create(
			name = "Graphic",
			duration_in_months = 9,
			start_date = datetime.date(2019,2,2),
			end_date = datetime.date(2019,11,30),
			description = "Visual representation of information",
		)
	def test_course_can_be_trained_by_a_teacher(self):
		self.javascript.teacher = self.teacher_a 
		self.assertEqual(self.python.teacher, self.teacher_a
		) 

	def test_many_courses_can_be_trained_by_one_trainer(self):
		self.javascript.teacher = self.teacher_b
		self.python.teacher = self.teacher_b
		self.assertEqual(self.javascript.teacher,self.python.teacher)

       


       
       
          	


	
   