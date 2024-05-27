from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from sfcsapp.models import FeedbackFacultyAdmin, FeedbackStudent


def facultyadmin_home(request):
    return render(request, "FACULTYADMIN/home.html")


def view_requests(request):
    return render(request, "FACULTYADMIN/view_requests.html")


def facultyadmin_feedback(request):
    return render(request, "FACULTYADMIN/feedback.html")


def facultyadmin_feedback_save(request):
    if request.method != "POST":
        return HttpResponseRedirect(reverse("facultyadmin_feedback_save"))
    else:
        feedback_msg = request.POST.get("feedback_msg")

        try:
            feedback = FeedbackStudent(student_id=student_id, feedback=feedback_msg, feedback_reply="")
            feedback.save()
            messages.success(request, "Successfully sent feedback")
            return HttpResponseRedirect("facultyadmin_feedback")
        except:
            messages.error(request, "Failed to send feedback")
            return HttpResponseRedirect("facultyadmin_feedback")


