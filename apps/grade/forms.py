from django.forms import forms
from django.core.exceptions import ValidationError


#自定义方法，检查是否是excel文件
def validate_excel(value):
 if value.name.split('.')[-1] not in ['xls','xlsx']:
    raise ValidationError(('格式错误: %(value)s'),params={'value': value},)

class FileForm(forms.Form):
    file_name = forms.FileField(validators=[validate_excel])