from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse
from sfcsapp.models import FacultyAdmin
from sfcsapp.models import Clearance
from sfcsapp.models import ClearanceReport
from sfcsapp.models import Student
from sfcsapp.models import FeedbackStudent
import datetime


def student_home(request):
    return render(request, "STUDENT/home.html")


def student_request_clearance(request):
    return render(request, "STUDENT/student_request_clearance.html")


def student_request_clearance_save(request):
    if request.method != "POST":
        return HttpResponseRedirect(reverse("student_request_clearance"))
    else:
        clearance_date = request.POST.get("clearance_date")


        try:
            clearance_report = ClearanceReport(student_id=student_obj, clearance_date=clearance_date)
            clearance_report.save()
            messages.success(request, "Successfully requested for clearance")
            return HttpResponseRedirect("/student_request_clearance")
        except:
            messages.error(request, "Failed to request for clearance")
            return HttpResponseRedirect("/student_request_clearance")


def student_feedback(request):
    return render(request, "STUDENT/feedback.html")


def student_feedback_save(request):
    if request.method != "POST":
        return HttpResponseRedirect(reverse("student_feedback_save"))
    else:
        feedback_msg = request.POST.get("feedback_msg")

        try:
            feedback = FeedbackStudent(student_id=student_id, feedback=feedback_msg, feedback_reply="")
            feedback.save()
            messages.success(request, "Successfully sent feedback")
            return HttpResponseRedirect("student_feedback")
        except:
            messages.error(request, "Failed to send feedback")
            return HttpResponseRedirect("student_feedback")
