import os
import random

from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
import xlrd
# Create your views here.
from .forms import FileForm,ExamSeatForm
from .models import StudentName,ExamSeat
from student.random_exam import main,CountProg


# Ajax返回错误信息
def Error(code, massage):
    data = {}
    data['status'] = 'ERROR'
    data['code'] = code
    data['massage'] = massage
    return JsonResponse(data)


# Ajax返回成功信息
def Success():
    data = {}
    data['status'] = 'SUCCESS'
    data['code'] = "随机排位完成"
    return JsonResponse(data)


class UpFileView(View):
    def get(self,request):
        return render(request,'test.html',{

        })
    def post(self,request):
        file_form = FileForm(request.POST, request.FILES)
        if file_form.is_valid():
            #获取上传文件的数据
            wb = xlrd.open_workbook(filename=None, file_contents=request.FILES['file_name'].read())
            #第一个表格
            table = wb.sheets()[0]

            row = table.nrows

            for i in range(1,row):
                #获取表格所有数据
                all_datil = table.row_values(i)

                add_student = StudentName()


                #班级名
                add_student.class_name = all_datil[0]
                #学号
                add_student.studnet_id = int(all_datil[1])
                #姓名
                add_student.student_name = all_datil[2]
                add_student.save()



            return render(request,'test.html',{

            })
        else:
            return render(request,'test.html',{
                'file_form':file_form

            })


#随机排考试座位表
class RandomExamSeatView(View):


    def get(self,request):
            return render(request, 'random_exam.html', {
                "Student_Count":StudentName.objects.all().count()

        })


    def post(self,request):
        all_class = request.POST.get('all_class','')
        all_exam = request.POST.get('all_exam','')
        if all_class or all_exam:
            main(all_class,all_exam)
            return Success()
        else:
            return Error(500,'输入错误')


#进度条
class Prog_Count(View):
    def post(self,request):
        data = {}
        cont_prog = CountProg()
        data['cont_prog'] = cont_prog
        return JsonResponse(data,safe=False)




