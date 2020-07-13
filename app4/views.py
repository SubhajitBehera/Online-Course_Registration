from django.db import IntegrityError
from django.shortcuts import render,redirect
from app4.models import StudentModel,LoginModel,ScheduleModel,Enroll
from django.contrib import messages

# Create your views here.
def showIndex(request):
    return render(request,'main.html')


def students_details(request):
    return render(request,'students1.html')


def logout(request):
    return redirect('main')


def student_login(request):
    return render(request,'student_login.html')


def login_check(request):
    un = request.POST.get("t1")
    pa = request.POST.get("t2")
    ty = 'student'
    try:
        LoginModel.objects.get(username=un,password=pa,type=ty)
        return render(request,"student_home.html",{"name":un})
    except LoginModel.DoesNotExist:
        messages.error(request,"Invalid User")
        return redirect('student_login')


def register(request):
    return render(request,'register.html')


def register_student(request):
    na = request.POST.get("t1")
    age = request.POST.get("t2")
    cno = request.POST.get("t3")
    gen = request.POST.get("t4")
    un = request.POST.get("t5")
    pa = request.POST.get("t6")
    type = 'student'

    sm = StudentModel(name=na, age=age, contactno=cno, gender=gen, username=un)
    sm.save()

    LoginModel(username=un, password=pa, type=type).save()

    # return render(request,"register.html",{"message":"Thanks For Registration"})

    messages.success(request, "Thanks For Registration")
    return redirect('register')


def admin_login(request):
    return render(request,'admin_login.html')


def check_admin(request):
    aname=request.POST.get("am1")
    apass=request.POST.get("am2")
    if aname=="Subha" and apass=="subha123":
     return render(request,'admin_welcome.html')
    else:
        return render(request,'admin_login.html',{"message":"Invalid Username and Password"})


def new_schedule(request):
    return render(request,'new_schedule.html')


def submit(request):
    na=request.POST.get("sc1")
    faculty=request.POST.get("sc2")
    dt=request.POST.get("sc3")
    time=request.POST.get("sc4")
    fee=request.POST.get("sc5")
    dur=request.POST.get("sc6")


    sm=ScheduleModel(name=na,faculty=faculty,date=dt,time=time,fee=fee,duration=dur).save()

    messages.success(request,'Course is added')

    return redirect('submit')


def view_all_class(request):
    return render(request,'view_all_class.html',{"data":ScheduleModel.objects.all()})


def contact_us(request):
    return render(request,'contact_us.html')


def enrol_course(request):
    return render(request,'enrole.html',{"data":ScheduleModel.objects.all()})


def enroll(request):
    name_c=request.GET.get('x1')
    cno=request.GET.get('x2')
    Enroll(course_name=name_c,faculty_name=cno).save()
    messages.success(request,'Course is Enrolled')
    return redirect('enrol_course')


def view_all_course(request):
    return render(request,'view_all_course.html',{"data":Enroll.objects.all()})


def cancel_enroled_course(request):
    return render(request,'delete_enroll_course.html',{"data":Enroll.objects.all()})


def delete(request):
      no = request.GET.get('cid')
      Enroll.objects.get(cid=no).delete()
      messages.success(request,'Course deleted Successfully')
      return redirect('cancel_enroled_course')

