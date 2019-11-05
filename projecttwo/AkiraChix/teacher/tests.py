from django.test import TestCase
from .models import Teacher
from teacher.forms import TeacherForm
import datetime
# Create your tests here.



class AddTeacherTestCase(TestCase):
    def setUp(self):
        self.data = {
        "first_name": "Irene",
	    "last_name": "Nyambura",
	    "date_of_birth": datetime.date(1996,6,19),
	    "gender": "female",
	    "registration_number": "4677",
	    "emails": "mwangiirene33@gmail.com",
	    "phone_number": "0717995920",
	    "date_joined": datetime.date.today(),
	    "profession": "Web Dev",
	    "id_number": "32925498",
        }

        self.bad_data ={

        "first_name": "Irene",
        "last_name": "Nyambura",
        "date_of_birth": datetime.date(1996,6,19),
        "gender": "female",
        "registration_number": "4677",
        "emails": "mwangiirene33gmail.com",
        "phone_number": "0717995920",
        "date_joined": datetime.date.today(),
        "profession": "Web Dev",
	    "id_number": "32925498",
        }


    def test_teacher_form_accepts_valid_data(self):
        form = TeacherForm(self.data)
        self.assertTrue(form.is_valid())
    
    def test_teacher_form_rejects_invalid_data(self):
        form = TeacherForm(self.bad_data)
        self.assertFalse(form.is_valid())    