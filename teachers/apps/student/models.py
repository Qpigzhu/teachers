from django.db import models

# Create your models here.

#上传文件
class UploadFile(models.Model):
    file_name = models.FileField(upload_to='student/%Y/%m/%d/', verbose_name=u"文件名称")


    class Meta:
        verbose_name = "上传文件管理"
        verbose_name_plural = verbose_name


#学生花名册
class StudentName(models.Model):
    class_name  = models.CharField(max_length=20,default="",verbose_name="班级")
    studnet_id = models.CharField(max_length=100,verbose_name="学号")
    student_name = models.CharField(max_length=15,verbose_name="名字")

    class Meta:
        verbose_name = "学生花名册"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "{}:{}".format(self.class_name,self.student_name)

#考试座位表
class ExamSeat(models.Model):
    studnet_id = models.CharField(max_length=100, verbose_name="学号")
    student_name = models.CharField(max_length=15, verbose_name="名字")
    class_name = models.CharField(max_length=20,verbose_name="考试班级")
    seat_number = models.IntegerField(null=True,blank=True,verbose_name="座位号")

    class Meta:
        verbose_name = "考试座位表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "{}:{}".format(self.class_name,self.student_name)
