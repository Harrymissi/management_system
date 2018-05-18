from django.shortcuts import render
from django.contrib.auth import authenticate,login   # 验证
from  django.contrib.auth.backends import ModelBackend
from .models import UserProfile, Rank_Record, Transaction, ClassInfo, ParentInfo, Attendance
from django.views.generic.base import View
from django.contrib.auth.hashers import make_password
from datetime import datetime
# Create your views here.

class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(username=username)
            if user.check_password(password):
                return user
        except Exception as e:
            return None



def user_login(request):
    if request.method=='POST':
        user_name=request.POST.get("username","")    # 取不到时候为空  username和password是前端页面账号名密码的name
        user_psw = request.POST.get("password", "")

        user=authenticate(username=user_name,password=user_psw)    #成功返回user对象,失败返回null



        student_name  = user_name

        if user is not None:        # 如果不是null说明验证成功

            student = UserProfile.objects.get(username=user_name)

            login(request,user)
            # login 两参数：request, user
            # 实际是对request写了一部分东西进去，然后在render的时候：
            # request是要render回去的。这些信息也就随着返回浏览器。完成登录
            # 跳转到首页 user request会被带回到首页

            return render(request,"usercenter-info.html",{
                "student_name":student_name,
                "student": student,

            })
            #登陆成功跳回首页
        else:
            return render(request,"login.html",{"msg":"username or password is wrong"})


    elif request.method=="GET":
        return render(request,"login.html",{

        })



def user_info(request):
    if request.method == "GET":
      stu_id = request.user.id
      student = UserProfile.objects.get(id = int(stu_id))
      current_page = "info"
      return render(request,"usercenter-info.html",{
        "student":student,
        "current_page":current_page
    })


def user_course(request):
    if request.method=="GET":
        stu_id = request.user.id
        student = UserProfile.objects.get(id=int(stu_id))
        current_page = "course"
        return render(request,"usercenter-mycourse.html",{
            "student" : student,
            "current_page": current_page
        })



def user_rank_record(request):
    if request.method=="GET":
        stu_id = request.user.id
        student_record = Rank_Record.objects.filter(std_num=int(stu_id))
        current_page = "rank"
        return render(request, "usercenter-message.html", {
            "student_record": student_record,
            "current_page": current_page
        })

def user_course_record(request):
    if request.method=="GET":
        stu_id = request.user.id
        student = Attendance.objects.filter(std_num=int(stu_id))
        current_page = "rank"
        return render(request, "usercenter-courserecord.html", {
            "student": student,
            "current_page": current_page
        })


def user_finance(request):
    if request.method=="GET":
        stu_id = request.user.id
        student = Transaction.objects.filter(std_num=int(stu_id))
        current_page = "finance"
        return render(request, "usercenter-finance.html", {
            "student": student,
            "current_page": current_page
        })


class user_pay(View):
    def post(self,request):
        user_id = request.user.id
        student1 = UserProfile.objects.get(id=int(user_id))

        tr_type = request.POST.get("type1","")
        tr_type2 = request.POST.get("type2","")
        tr_amount = request.POST.get("amount","")

        tr_record = Transaction()

        if tr_type == "product":
            tr_record.tr_type = "purchasing products"
            tr_record.tr_amount = tr_amount
            tr_record.tr_date = datetime.now()
            tr_record.std_num = student1
            tr_record.save()

        elif tr_type == "test":
            tr_record.tr_type = "tests"
            tr_record.tr_amount = tr_amount
            tr_record.tr_date = datetime.now()
            tr_record.std_num = student1
            tr_record.save()

        elif tr_type == "membership":
            if tr_type2 == "beginner":
                stu_class = ClassInfo.objects.get(class_level="beginner")
                student1.stu_class = stu_class
                tr_record.tr_type = tr_type
                tr_record.tr_amount = tr_amount
                tr_record.tr_date = datetime.now()
                tr_record.std_num = student1
                tr_record.save()
                student1.save()
            elif tr_type2 == "intermediate":
                stu_class = ClassInfo.objects.get(class_level="intermediate")
                student1.stu_class = stu_class
                tr_record.tr_type = tr_type
                tr_record.tr_amount = tr_amount
                tr_record.tr_date = datetime.now()
                tr_record.std_num = student1
                tr_record.save()
                student1.save()
            else:
                stu_class = ClassInfo.objects.get(class_level="advanced")
                student1.stu_class = stu_class
                tr_record.tr_type = tr_type
                tr_record.tr_amount = tr_amount
                tr_record.tr_date = datetime.now()
                tr_record.std_num = student1
                tr_record.save()
                student1.save()
        student = Transaction.objects.filter(std_num=int(user_id))

        return render(request,"usercenter-finance.html",{
            "student":student,

        })

    def get(self,request):
        return render(request, "usercenter-pay.html", {

        })



class user_register(View):
    def post(self,request):
        user_name = request.POST.get("username","")
        user_psw =request.POST.get("password","")
        user_psw1 =request.POST.get("password1","")
        user_add = request.POST.get("address","")

        if user_psw != user_psw1:
            return render(request,'register.html',{
                "msg":"Two input password must be consistent ",
            })
        else:
            user = UserProfile()
            user.username = user_name
            user.password = make_password(user_psw)
            user.date_joined = datetime.now()
            user.address = user_add
            user.save()


            student = UserProfile.objects.get(username=user_name)

            rank_record = Rank_Record()
            rank_record.RD_color = "White"
            rank_record.RD_date= datetime.now()
            rank_record.std_num=student
            rank_record.save()

            return render(request,"login.html")

    def get(self,request):
        return render(request,"register.html",{})


class user_parent(View):
    def post(self,request):
        parent_name = request.POST.get("parent_name","")
        parent_phone  = request.POST.get("phone","")
        parent_email = request.POST.get("email","")
        user_id = request.user.id
        student1 = UserProfile.objects.get(id=int(user_id))

        parent = ParentInfo()
        parent.name = parent_name
        parent.email = parent_email
        parent.phone = parent_phone
        parent.std_num = student1
        parent.save()

        parent1 = ParentInfo.objects.get(std_num=int(user_id))

        current_page = "parent_page"

        return render(request,"usercenter-parent.html",{
            "parent":parent1,
            "current_page": current_page,
        })

    def get(self,request):
        user_id = request.user.id

        current_page = "parent_page"


        try: ParentInfo.objects.get(std_num=int(user_id))

        except:

            return render(request, "usercenter-parent.html", {

                "current_page": current_page,
            })

        parent = ParentInfo.objects.get(std_num=int(user_id))
        return render(request, "usercenter-parent.html", {
            "parent":parent,
            "current_page": current_page,
        })







