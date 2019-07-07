from django.shortcuts import redirect
from django.shortcuts import render
from .forms import StudentForm
from .models import Student


def add_student(request):
	if request.method == "POST":
		form = StudentForm(request.POST)
		if form.is_valid():
			form.save()

	else:
		form = StudentForm()

	return render(request,"add_student.html",{"form":form})

def list_students(request):
	students = Student.objects.all()
	return render(request,"all_students.html",{"students":students})	

def student_details(request,pk):
	student = Student.objects.get(pk=pk)
	Courses = student.Courses.all()
	return render(request,"student_details.html",{"student":student})
	# ,"Courses":Courses

def edit_student(request,pk):
		student = Student.objects.get(pk=pk)
		if request.method == "POST":
			form = StudentForm(request.POST,instance=student)
			if form.is_valid:
				form.save()
				return redirect("list_students")
		else:
			form = StudentForm(instance=student)

		return render(request,"edit_student.html",{"form":form})			
# Create your views here.