from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from sfcsapp.models import CustomUser, FacultyAdmin, Faculty, Courses, Student


def admin_home(request):
    return render(request, "HOD/home.html")


def add_facultyadmin(request):
    return render(request, "HOD/add_facultyadmin.html")


def add_facultyadmin_save(request):
    if request.method!="POST":
        return HttpResponse("Method not allowed")
    else:
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        try:
            user = CustomUser.objects.create_user(username=username, password=password,
                                              email=email, last_name=last_name, first_name=first_name, user_type=2)
            user.save()
            messages.success(request, "Successfully Added Administrator")
            return HttpResponseRedirect("/add_facultyadmin")
        except:
            messages.error(request, "Failed to add Administrator")
            return HttpResponseRedirect("/add_facultyadmin")


def add_faculty(request):
    return render(request, "HOD/add_faculty.html")


def add_faculty_save(request):
    if request.method!="POST":
        return HttpResponseRedirect("Method Not Allowed")
    else:
        faculty = request.POST.get("faculty")
        try:
            faculty_model = Faculty(name=faculty)
            faculty_model.save()
            messages.success(request, "Successfully added Faculty")
            return HttpResponseRedirect("/add_faculty")
        except:
            messages.error(request, "Failed to add Faculty")
            return HttpResponseRedirect("/add_faculty")


def add_course(request):
    faculty = Faculty.objects.all()
    return render(request, "HOD/add_course.html", {"faculty":faculty})


def add_course_save(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method not allowed</h2>")
    else:
        course_name = request.POST.get("course_name")
        faculty_id = request.POST.get("faculty")


        try:
            courses_model = Courses(course_name=course_name, faculty_id=faculty)
            courses_model.save()
            messages.success(request, "Successfully added course")
            return HttpResponseRedirect("/add_course")
        except:
            messages.error(request, "Failed to add course")
            return HttpResponseRedirect("/add_course")


def add_student(request):
    courses = Courses.objects.all()
    return render(request, "HOD/add_student.html", {"courses":courses})


def add_student_save(request):
    if request.method!="POST":
        return HttpResponse("Method not allowed")
    else:
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        course_id = request.POST.get("course")
        gender = request.POST.get("gender")
        try:
            user = CustomUser.objects.create_user(username=username, password=password,
                                              email=email, last_name=last_name, first_name=first_name, user_type=3)
            course_obj = Courses.objects.get(id=course_id)
            user.student.course_id = course_obj
            user.student.gender = gender
            user.student.profile_pic = ""
            user.save()
            messages.success(request, "Successfully Added Student")
            return HttpResponseRedirect("/add_student")
        except:
            messages.error(request, "Failed to add Student")
            return HttpResponseRedirect("/add_student")


def manage_facultyadmin(request):
    facultyadmin = FacultyAdmin.objects.all()
    return render(request, "HOD/manage_facultyadmin.html", {"FacultyAdmin": FacultyAdmin})


def manage_student(request):
    student = Student.objects.all()
    return render(request, "HOD/manage_student.html", {"student":student})


def manage_faculty(request):
    faculty = Faculty.objects.all()
    return render(request, "HOD/manage_faculty.html", {"faculty":faculty})


def manage_course(request):
    courses = Courses.objects.all()
    return render(request, "HOD/manage_course.html", {"courses":courses})


def edit_faculty(request, faculty_id):
    faculty = Faculty.objects.get(id=faculty_id)
    return render(request, "HOD/edit_faculty.html", {"faculty":faculty})


def edit_faculty_save(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        name = request.POST.get("name")
        faculty_id = request.POST.get("faculty_id")

        try:
            faculty.name = name
            faculty.id = faculty_id
            faculty.save()

            messages.success(request, "Successfully edited faculty")
            return HttpResponseRedirect("/edit_faculty/"+faculty_id)
        except:
            messages.error(request, "Failed to edit faculty")
            return HttpResponseRedirect("/edit_faculty")


def edit_student(request, student_id):
    student = Student.objects.all
    return render(request, "HOD/edit_student.html", {"student":student})


def edit_student_save(request):
    if render.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        student_id = request.POST.get("student_id")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        course_id = request.POST.get("course")
        gender = request.POST.get("gender")

        try:
             user = CustomUser.objects.get(id=student_id)
             user.first_name = first_name
             user.last_name = last_name
             user.username = username
             user.email = email
             user.save()

             student = Student.objects.get(admin=student_id)
             student.gender = gender
             course = Courses.objects.get(id=course_id)
             student.course_id = course
             student.save()
             messages.success(request, "Successfully edited Student")
             return HttpResponseRedirect("/edit_student/"+student_id)
        except:
            messages.error(request, "Failed to edit student")
            return HttpResponseRedirect("/edit_student/"+student_id)














