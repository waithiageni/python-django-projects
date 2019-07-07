from django.db import models

class Teacher(models.Model):
	first_name = models.CharField(max_length = 50)
	last_name = models.CharField(max_length = 50)
	date_of_birth = models.DateField()
	gender = models.CharField(max_length = 20)
	registration_number = models.CharField(max_length = 20)
	emails = models.EmailField(max_length = 70)
	phone_number = models.CharField(max_length = 20)
	date_joined = models.DateField()
	# number_of_units = models.CharField(max_length = 5)
	profession = models.CharField(max_length = 20,null = True)
	id_number = models.SmallIntegerField(null = True)

	def __str__(self):
		return self.first_name + " " + self.last_name


# Create your models here.
