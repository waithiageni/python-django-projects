from django.contrib import admin
from .models import Teacher


class TeacherAdmin(admin.ModelAdmin):
	list_display = ("first_name","last_name","registration_number","emails","profession")
	search_fields = ("first_name","last_name","registration_number","emails","profession")

admin.site.register(Teacher,TeacherAdmin)


# Register your models here.
