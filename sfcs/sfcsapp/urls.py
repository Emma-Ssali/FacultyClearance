from django.urls import path
from .views import showDemoPage, ShowLoginPage

urlpatterns = [
    path('demo', showDemoPage, name="demo-page"),
    path('login_page', ShowLoginPage, name="login-page"),
]


