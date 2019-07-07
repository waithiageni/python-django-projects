from django.urls import path
from .views import add_Course
from .views import list_Courses
from .views import Course_details
from .views import edit_Course

urlpatterns = [
	path("add/",add_Course,name="add_Course"),
	path("list/",list_Courses,name ="list_Courses"),
	path("view/<int:pk>/",Course_details,name="Course_details"),
	path("edit/<int:pk>/",edit_Course,name="edit_Course"),
]