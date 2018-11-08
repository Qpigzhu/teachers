import os
import random

from django.shortcuts import render
from django.views import View
import xlrd
# Create your views here.
from .forms import FileForm
from .models import StudentName,ExamSeat

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
        #控制循环开关，直到随机排完座位停止
        Bool_Complete = True
        #座位号
        SeatNumber = 1
        #取出所有学生
        all_student = StudentName.objects.all()
        #总数数字的列表
        random_number = [ i for i in range(0,all_student.count())]
        print(random_number)

        #随机班级
        class_number = [i for i in range(1,7)]


        while Bool_Complete:
            if SeatNumber % 31 == 0:
                SeatNumber = 1
            #判断是否完成排完
            if ExamSeat.objects.all().count() == all_student.count():
                break
            else:
                # 随机从总数数字列表中取出一个元素
                random_studnet = random.sample(random_number, 1)[0]
                # 随机在列表取出一个学生对象
                random_studnet = all_student[random_studnet]

                #当数据少于2的时，需要添加数据才可以判断
                if ExamSeat.objects.all().count() < 2:
                    # 随机取出一个班级
                    random_class_exam = random.sample(class_number, 1)[0]
                    add_examseat = ExamSeat()
                    add_examseat.class_name = random_class_exam
                    add_examseat.studnet_id = random_studnet.studnet_id
                    add_examseat.seat_number = SeatNumber
                    add_examseat.student_name = random_studnet.student_name
                    add_examseat.save()
                    SeatNumber += 1
                else:
                    # 取出最后一个学生对象，判断是否与前一个座位班级相同
                    exame_set = ExamSeat.objects.all().last()
                    if random_studnet.class_name == exame_set.class_name:
                        pass
                    else:

                        #随机取出一个班级
                        random_class_exam = random.sample(class_number, 1)[0]

                        if ExamSeat.objects.filter(seat_number=SeatNumber,class_name=random_class_exam):
                            pass

                        else:
                            add_examseat = ExamSeat()
                            add_examseat.class_name = random_class_exam
                            add_examseat.studnet_id = random_studnet.studnet_id
                            add_examseat.seat_number = SeatNumber
                            add_examseat.student_name = random_studnet.student_name
                            add_examseat.save()
                            SeatNumber += 1

        return render(request,'test.html',{
                "msg":"完成"
        })