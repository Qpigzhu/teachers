# _*_ encoding:utf-8 _*_
__author__ = 'pig'
__data__ = '2018\11\7 0007 19:59$'

import xadmin
from xadmin import views

from .models import StudentName,ExamSeat


class BaseSetting(object):
    # 开启主题功能
    enable_themes = True
    use_bootswatch = True


# xadmin 全局配置参数信息设置
class GlobalSettings(object):
    site_title = "Pig管理"
    site_footer = "Pig"
    #收起菜单
    menu_style = "accordion"



class StudentNameAdmin(object):
    list_dispaly = ['class_name','studnet_id','student_name']
    search_fields = ['class_name','studnet_id','student_name']
    list_filter = ['class_name','studnet_id','student_name']

class ExamSeatAdmin(object):
    list_dispaly = ['studnet_id','student_name','class_name','seat_number']
    search_fields = ['studnet_id','student_name','class_name','seat_number']
    list_filter = ['studnet_id','student_name','class_name','seat_number']


xadmin.site.register(StudentName,StudentNameAdmin)
xadmin.site.register(ExamSeat,ExamSeatAdmin)

# 将开启主题功能注册
xadmin.site.register(views.BaseAdminView,BaseSetting)
# 将头部与脚部信息进行注册:
xadmin.site.register(views.CommAdminView,GlobalSettings)