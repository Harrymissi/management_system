from django.contrib import admin
from .models import UserProfile,ParentInfo,ClassInfo,Rank_Record,Attendance,Transaction
import xadmin
from xadmin import views
# Register your models here.

class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True

xadmin.site.register(views.BaseAdminView,BaseSetting)


class GlobalSettings(object):
    site_title="Martial Management System"   #修改左上角名称和底角名称
    site_footer="Martial Art School"
    menu_style = "accordion"

xadmin.site.register(views.CommAdminView,GlobalSettings)



class ParentInfoAdmin(object):
    search_fields = ['std_num__username','name']
    list_filter = ['std_num__username','name','phone','email']
    list_display = ['name','phone','email','std_num']

xadmin.site.register(ParentInfo,ParentInfoAdmin)


class ClassInfoAdmin(object):
    search_fields = ['class_day', 'class_level']
    list_filter = ['class_day', 'class_level','class_time']
    list_display = ['class_level','class_day', 'class_time']

xadmin.site.register(ClassInfo,ClassInfoAdmin)

class Rand_RecordAdmin(object):
    search_fields = ['RD_color', 'std_num']
    list_filter = ['RD_color', 'std_num','RD_date']
    list_display = ['RD_color', 'std_num','RD_date']

xadmin.site.register(Rank_Record,Rand_RecordAdmin)

class AttendanceAdmin(object):
    search_fields = ['c_id', 'std_num']
    list_filter = ['c_id', 'std_num','Att_date']
    list_display = ['c_id', 'std_num','Att_date']

xadmin.site.register(Attendance,AttendanceAdmin)


class TransactionAdmin(object):
    search_fields = ['tr_type', 'std_num__username']
    list_filter = ['tr_type', 'std_num__username','tr_amount','tr_date']
    list_display = [ 'std_num','tr_type','tr_amount','tr_date']

xadmin.site.register(Transaction,TransactionAdmin)

