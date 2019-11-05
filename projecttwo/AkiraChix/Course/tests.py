from django.test import TestCase
from Course.models import Course
from Course.forms import CourseForm
import datetime

# Create your tests here.


class AddCourseTestCase(TestCase):
	def setUp(self):
		self.data = {
		"name" : "Python",
		"duration" : 9, 
		"start_date" : datetime.date.today(),
		"end_date" : datetime.date.today(), 
		"description" : "programming language",
		 

		}

		self.bad_data ={
		"name" : "Python",
		"duration" : 9, 
		"start_date" : datetime.date.today(),
		"end_date" : datetime.date.today(), 
		"description" : 96,
		"teacher" : "Nim"
		}

	def test_course_form_accepts_valid_data(self):
		form = CourseForm(self.data)
		self.assertTrue(form.is_valid())

	def test_course_form_rejects_invalid_data(self):
		form = CourseForm(self.bad_data)
		self.assertFalse(form.is_valid())


    # def test_course_form_rejects_invalid_data(self):
    #     form = CourseForm(self.bad_data)
    #     self.assertFalse(form.is_valid()) 