from django.contrib import admin
from .models import Course

class CourseAdmin(admin.ModelAdmin):
	list_display = ("name","description","duration","teacher")
	search_fields = ("name","description","duration","teacher__first_name")

admin.site.register(Course,CourseAdmin)
# Register your models here.
