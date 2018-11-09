import xadmin

from .models import Grade,Subject



class GradeAdmin(object):
    list_dispaly = ['class_name','student_id','student_name','chinese','math','english','politics','history','geography',
                    'physics','chemistry','biology','sports','TotalScore','conversion','type_of_examination']
    search_fields = ['class_name','student_id','student_name','chinese','math','english','politics','history','geography',
                    'physics','chemistry','biology','sports','TotalScore','conversion','type_of_examination']
    list_filter = ['class_name','student_id','student_name','chinese','math','english','politics','history','geography',
                    'physics','chemistry','biology','sports','TotalScore','conversion','type_of_examination']


class SubjectAdmin(object):
    list_dispaly = ["subject_name"]
    search_fields = ["subject_name"]
    list_filter = ["subject_name"]


xadmin.site.register(Grade,GradeAdmin)
xadmin.site.register(Subject,SubjectAdmin)