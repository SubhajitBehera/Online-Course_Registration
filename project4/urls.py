"""project4 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from app4 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.showIndex, name='main'),
    path('students_details/', views.students_details, name='students_details'),

    path('logout/', views.logout, name='logout'),
    path('student_login/', views.student_login, name='student_login'),

    path('login_check/', views.login_check, name='login_check'),
    path('register/', views.register, name='register'),

    path('register_student/', views.register_student, name='register_student'),
    path('admin_login/', views.admin_login, name='admin_login'),

    path('check_admin/', views.check_admin, name='check_admin'),
    path('new_schedule/', views.new_schedule, name='new_schedule'),

    path('submit/', views.submit, name='submit'),
    path('view_all_class/', views.view_all_class, name='view_all_class'),

    path('contact_us/', views.contact_us, name='contact_us'),
    path('enrol_course/', views.enrol_course, name="enrol_course"),

    path('enroll/', views.enroll, name='enroll'),
    path('view_all_course/', views.view_all_course, name='view_all_course'),

    path('cancel_enroled_course/', views.cancel_enroled_course, name='cancel_enroled_course'),
    path('delete/', views.delete, name='delete')
]
