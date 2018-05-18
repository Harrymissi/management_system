from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
# Create your models here.

class ClassInfo(models.Model):
    class_time = models.DateTimeField(verbose_name="Class time",blank=True,null=True)
    class_day = models.CharField(verbose_name="Class day", choices=(("Monday","Monday"),("Tuesday","Tuesday"),("Wendsday","Wendsday"),
                                                                    ("Thursday","Thursday"),("Friday","Friday"),("Saturday","Saturday"),
                                                                    ("Sunday","Sunday"),("No Class so far","No Class so far")),max_length=20,default="No Class so far")
    class_level = models.CharField(verbose_name="Level", choices=(("Beginner","Beginner"),("Intermediate","intermediate"),("Advanced","Advanced"),
                                                                  ("No Class","No Class"))
                                   ,max_length=50)

    class Meta:
        verbose_name = "Class Info"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.class_level


class UserProfile(AbstractUser):
    address = models.CharField(max_length=50,verbose_name="address",default="")
    image = models.ImageField(upload_to="image/%Y/%m",default="image/default.png",max_length=100)
    stu_class = models.ForeignKey(ClassInfo,verbose_name="Student's Class",on_delete=models.CASCADE,
                                  default=4)

    class Meta:
        verbose_name = "Students Info"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username    # username is from AbstractUser

class ParentInfo(models.Model):
    name = models.CharField(max_length=20,verbose_name="Name",default='')
    phone = models.CharField(max_length=10,verbose_name="Phone",null=True,blank=True)
    email = models.EmailField(max_length=50, verbose_name="Email")
    std_num = models.ForeignKey(UserProfile,verbose_name="Student's Name",on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Parent Info"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name



class Transaction(models.Model):
    tr_type = models.CharField(verbose_name="Transaction Type", choices=(("membership","membership"),("tests","tests"),
                                                                         ("purchasing products","purchasing products")),max_length=50)
    tr_date = models.DateTimeField(verbose_name="Transaction Date")
    tr_amount = models.IntegerField(verbose_name="Transaction Amount",default=0)
    std_num = models.ForeignKey(UserProfile, verbose_name="Student's Name", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Transaction Info"
        verbose_name_plural = verbose_name




class Attendance(models.Model):
    std_num = models.ForeignKey(UserProfile, verbose_name="Student's Name", on_delete=models.CASCADE)
    c_id = models.ForeignKey(ClassInfo, verbose_name="Class' ID", on_delete=models.CASCADE)
    Att_date = models.DateTimeField(verbose_name="Attendance Date")

    class Meta:
        verbose_name = "Attendance Info"
        verbose_name_plural = verbose_name




class Rank_Record(models.Model):
    RD_color = models.CharField(verbose_name="Rank Colors", default="White",
                                choices=(("White","White"),("Yellow","Yellow"),("Half Green","Half Green"),
                                         ("Green","Green"),("Half Blue","Half Blue"),("Blue","Blue"),
                                         ("Half Red","Half Red"),("Red","Red"),("Half Black","Half Black"),("Black","Black")),max_length=50)
    RD_date = models.DateTimeField(verbose_name="Rank Record Date",default=datetime.now)
    std_num = models.ForeignKey(UserProfile, verbose_name="Student's Name", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Rank Record Info"
        verbose_name_plural = verbose_name


