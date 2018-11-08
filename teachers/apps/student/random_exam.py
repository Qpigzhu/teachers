# _*_ encoding:utf-8 _*_
__author__ = 'pig'
__data__ = '2018\11\8 0008 12:44$'
"""
随机排考试座位接口
"""
import random
import os,django
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "teachers.settings")
django.setup()

from student.models import StudentName,ExamSeat


def add_new_examseat(class_name,studnet_id,seat_number,student_name):
    """
    向数据库添加考试座位表数据
    :教室名 class_name:
    :学号 studnet_id:
    :座位表 seat_number:
    :学生名字 student_name:
    """
    add_examseats = ExamSeat()
    add_examseats.class_name = class_name
    add_examseats.studnet_id = studnet_id
    add_examseats.seat_number = seat_number
    add_examseats.student_name = student_name
    add_examseats.save()


def main(all_class,all_seatnumber):
    """

    :每个课室的座位总数 all_seatnumber:
    :一共多少个考场 all_class:
    :return 成功200:
    """
    #每个课室的座位总数
    all_seatnumber = all_seatnumber + 1

    # 控制循环开关，直到随机排完座位停止
    Bool_Complete = True
    # 座位号
    SeatNumber = 1
    # 取出所有学生
    all_student = StudentName.objects.all()
    # 总数数字的列表
    random_number = [i for i in range(0, all_student.count())]
    print(random_number)

    # 随机班级列表
    class_number = [i for i in range(1, all_class+1)]

    while Bool_Complete:
        #控制每一个班座位
        if SeatNumber % all_seatnumber == 0:
            SeatNumber = 1
        # 判断是否完成排完
        if ExamSeat.objects.all().count() == all_student.count():
            Bool_Complete = False
        else:
            # 随机从总数数字列表中取出一个元素
            random_studnet = random.sample(random_number, 1)[0]
            # 随机在列表取出一个学生对象
            random_studnet = all_student[random_studnet]

            # 当数据少于2的时，需要添加数据才可以判断
            if ExamSeat.objects.all().count() < 2:
                # 随机取出一个班级
                random_class_exam = random.sample(class_number, 1)[0]
                add_new_examseat(random_class_exam,random_studnet.studnet_id,SeatNumber,random_studnet.student_name)
                SeatNumber += 1
            else:
                #取出最后一个学生对象，判断是否与前一个座位班级相同
                exame_set = ExamSeat.objects.all().last()
                if random_studnet.class_name == exame_set.class_name:
                    pass


                # 随机取出一个班级
                random_class_exam = random.sample(class_number, 1)[0]

                if ExamSeat.objects.filter(seat_number=SeatNumber, class_name=random_class_exam):
                    pass

                else:
                    add_new_examseat(random_class_exam, random_studnet.studnet_id, SeatNumber,
                                     random_studnet.student_name)
                    SeatNumber += 1

    return 200


if __name__ == '__main__':
    a = main()
    print(a)

