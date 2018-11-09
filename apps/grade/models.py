from django.db import models

# Create your models here.
class Grade(models.Model):
    class_name = models.CharField(max_length=20,verbose_name="班级")
    student_id = models.CharField(max_length=50,verbose_name="学号")
    student_name = models.CharField(max_length=15,verbose_name="姓名")
    chinese = models.FloatField(default=0,verbose_name="语文")
    math = models.FloatField(default=0,verbose_name="数学")
    english = models.FloatField(default=0,verbose_name="英语")
    politics = models.FloatField(default=0,verbose_name="政治")
    history = models.FloatField(default=0,verbose_name="历史")
    geography = models.FloatField(default=0,verbose_name="地理")
    physics = models.FloatField(default=0,verbose_name="物理")
    chemistry = models.FloatField(default=0,verbose_name="化学")
    biology = models.FloatField(default=0,verbose_name="生物")
    sports = models.FloatField(default=0,verbose_name="体育")
    TotalScore = models.FloatField(default=0,verbose_name="总分")
    conversion = models.FloatField(default=0,verbose_name="折算后的分数")
    type_of_examination = models.CharField(max_length=50,verbose_name="考试类型")


    class Meta:
        verbose_name = "学生成绩表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.student_name


class Subject(models.Model):
    subject_name = models.CharField(max_length=15,verbose_name="科目")

    class Meta:
        verbose_name = "科目"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.subject_name