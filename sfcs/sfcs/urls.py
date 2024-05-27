"""
URL configuration for sfcs project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from sfcs import settings
from sfcsapp import views, AdminViews, FacultyAdminViews, StudentViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login_page', views.ShowLoginPage),
    path('get_user_details', views.GetUserDetails),
    path('logout_user', views.logout_user),
    path('dologin', views.doLogin),
    path('HOD_home', AdminViews.admin_home),
    path('add_facultyadmin', AdminViews.add_facultyadmin),
    path('add_facultyadmin_save', AdminViews.add_facultyadmin_save),
    path('add_faculty', AdminViews.add_faculty),
    path('add_faculty_save', AdminViews.add_faculty_save),
    path('add_course', AdminViews.add_course),
    path('add_course_save', AdminViews.add_course_save),
    path('add_student', AdminViews.add_student),
    path('add_student_save', AdminViews.add_student_save),
    path('manage_facultyadmin', AdminViews.manage_facultyadmin),
    path('manage_student', AdminViews.manage_student),
    path("manage_faculty", AdminViews.manage_faculty),
    path("manage_course", AdminViews.manage_course),
    path("edit_faculty/<str:faculty_id>", AdminViews.edit_faculty),
    path("edit_faculty_save", AdminViews.edit_faculty_save),
    path("edit_student/<str:student_id>", AdminViews.edit_student),
    # FACULTYADMIN URL PATH
    path("facultyadmin_home", FacultyAdminViews.facultyadmin_home, name="facultyadmin_home"),
    path("view_requests", FacultyAdminViews.view_requests, name="view_requests"),
    path("facultyadmin_feedback", FacultyAdminViews.facultyadmin_feedback, name="facultyadmin_feedback"),
    path("facultyadmin_feedback_save", FacultyAdminViews.facultyadmin_feedback_save, name="facultyadmin_feedback_save"),
    # STUDENT URL PATH
    path("student_home", StudentViews.student_home, name="student_home"),
    path("student_request_clearance", StudentViews.student_request_clearance, name="student_request_clearance"),
    path("student_request_clearance_save", StudentViews.student_request_clearance_save, name="student_request_clearance_save"),
    path("student_feedback", StudentViews.student_feedback, name="student_feedback"),
    path("student_feedback_save", StudentViews.student_feedback_save, name="student_feedback_save"),
]+static(settings.MEDIA_URL,
         document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

