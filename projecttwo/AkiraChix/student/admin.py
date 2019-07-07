from django.contrib import admin
from .models import Student

class StudentAdmin(admin.ModelAdmin):
	list_display = ("registration_number","first_name","last_name","date_of_birth","emails")
	search_fields = ("registration_number","first_name","last_name","emails")


    
 
admin.site.register(Student,StudentAdmin)


# Register your models here.
