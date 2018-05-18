"""martial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
import xadmin
from  django.views.generic import TemplateView
from students.views import user_login, user_course, user_rank_record, user_finance,user_info,user_register,user_pay,user_parent,user_course_record

urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path('index/',TemplateView.as_view(template_name="index.html"),name = "index"),
    path('login/',user_login,name = "login"),  #login 不加括号 是表明只指向这个函数  加括号是调用这个函数
    path('course/',user_course,name="course"),
    path('success/',user_rank_record,name="success"),
    path('course-record/',user_course_record,name="course-record"),
    path('finance/',user_finance,name="finance"),
    path('pay/', user_pay.as_view(), name="pay"),
    path('info/',user_info,name="info"),
    path('register/',user_register.as_view(),name = "register"),
    path('parent/',user_parent.as_view(),name = "parent"),

]
