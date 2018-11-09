import xlrd

from django.shortcuts import render
from django.views import View
from django.http import JsonResponse

from .models import Grade,Subject
from .forms import FileForm


#计算进度条全局变量
Row = 0 #数据总行数
SaveNumber = 0 #数据已录入数量


# Create your views here.
def add_grade_subject(student_id,subject,subject_grade):
    """
    录入科目成绩

    :学生学号 student_id:
    :科目名称 subject:
    :科目成绩 subject_grade:
    :错误返回0:
    """
    #如果找不到该学生，返回0
    try:
        add_grade = Grade.objects.get(student_id=student_id)
    except:
        return 0
    if subject == "语文":
        add_grade.chinese = subject_grade
    elif subject == "英语":
        add_grade.english = subject_grade
    elif subject == "数学":
        add_grade.math = subject_grade
    elif subject == "生物":
        add_grade.biology = subject_grade
    elif subject == "历史":
        add_grade.history = subject_grade
    elif subject == "政治":
        add_grade.politics =subject_grade
    elif subject == "地理":
        add_grade.geography  = subject_grade
    elif subject == "化学":
        add_grade.chemistry = subject_grade
    elif subject == "物理":
        add_grade.physics = subject_grade
    elif subject == "体育":
        add_grade.sports = subject_grade

    add_grade.save()










class EntryGradeView(View):
    def get(self,request):
        all_subject = Subject.objects.all()
        return render(request,'mark.html',{
            "all_subject":all_subject
        })

    def post(self,request):

        global Row,SaveNumber
        file_form = FileForm(request.POST,request.FILES)
        all_subject = Subject.objects.all()
        if file_form.is_valid():
            #获取科目名称
            subject_name = request.POST.get("subject","")
            # 获取上传文件的数据
            wb = xlrd.open_workbook(filename=None, file_contents=request.FILES['file_name'].read())

            #第一个表格
            table = wb.sheets()[0]
            #获取总行数
            row = table.nrows
            Row = row

            for i in range(2,row):
                #打印表格所有内容
                all_datil = table.row_values(i)

                #是否有该学生的数据,没有就创建该学生数据
                if not Grade.objects.filter(student_id=all_datil[0]):
                    add_grade = Grade()
                    add_grade.student_name = all_datil[1]
                    add_grade.class_name = all_datil[2]
                    add_grade.student_id = all_datil[0]
                    add_grade.save()

                    #录入科目成绩
                    add_grade_subject(all_datil[0],subject_name,all_datil[3])
                    SaveNumber +=1

                else:
                    add_grade_subject(all_datil[0], subject_name, all_datil[3])
                    SaveNumber +=1

            return render(request,'mark.html',{
                "all_subject": all_subject,
                "msg":"成功录入"
            })

        else:
            return render(request,'mark.html',{
                "all_subject": all_subject,
                "file_form":file_form
            })

class ProgCount(View):
    def progcount(self,request):
        global Row,SaveNumber
        data = {}
        cont_prog = int((SaveNumber / Row) * 100)
        data['cont_prog'] = cont_prog
        return JsonResponse(data, safe=False)