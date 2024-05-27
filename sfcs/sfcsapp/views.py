from django.contrib.auth import authenticate, login, logout
from django.core.checks import messages
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
import datetime

from django.urls import reverse
from sfcsapp.EmailBackEnd import EmailBackEnd


# Create your views here.





def ShowLoginPage(request):
    return render(request, "login_page.html")


def doLogin(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        user = EmailBackEnd.authenticate(request, username=request.POST.get("email"), password=request.POST.get("password"))
        if user!=None:
            login(request, user)
            if user.user_type == "1":
                return HttpResponseRedirect('/HOD_home')
            elif user.user_type == "2":
                return HttpResponseRedirect(reverse("facultyadmin_home"))
            else:
                return HttpResponseRedirect(reverse("student_home"))
        else:
            messages.error(request, "Invalid Login Details")
            return HttpResponseRedirect("/")


def GetUserDetails(request):
    if request.user!=None:
        return HttpResponse("User : "+request.user.email+" usertype : "+request.user.user_type)
    else:
        return HttpResponse("Please login first")


def logout_user(request):
    logout(request)
    return HttpResponseRedirect("/")







