# _*_ encoding:utf-8 _*_
__author__ = 'pig'
__data__ = '2018\11\7 0007 20:21$'

from django import forms
from django.core.exceptions import ValidationError

#自定义方法，检查是否是excel文件
def validate_excel(value):
 if value.name.split('.')[-1] not in ['xls','xlsx']:
    raise ValidationError(('格式错误: %(value)s'),params={'value': value},)

class FileForm(forms.Form):
    file_name = forms.FileField(validators=[validate_excel])


class ExamSeatForm(forms.Form):
    all_class = forms.IntegerField(required=True)
    all_exam = forms.IntegerField(required=True)
