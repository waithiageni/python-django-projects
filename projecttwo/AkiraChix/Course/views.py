from django.shortcuts import render
from django.shortcuts import redirect
from .forms import CourseForm
from .models import Course


def add_Course(request):
	if request.method == "POST":
		form = CourseForm(request.POST)
		if form.is_valid():
			form.save()

	else:
		form = CourseForm()		
	# form = CourseForm()
	return render(request,"add_Course.html",{"form":form})

def list_Courses(request):
	Courses = Course.objects.all()
	return render(request,"all_Course.html",{"Courses":Courses})
	
def Course_details(request,pk):
	Course = Course.objects.get(pk=pk)
	return render(request,"Course_details.html",{"Course":Course})

def edit_Course(request,pk):
	Course =Course.objects.get(pk=pk)
	if request.method =="POST":
		form = CourseForm(request.POST,instance=Course)
		if form.is_valid:
			form.save()
			return redirect("list_Courses")
		else:
			form = CourseForm(instance=Course)

		return render(request,"edit_Course.html",{"form":form})		
# Create your views here.
