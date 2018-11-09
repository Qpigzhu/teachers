from django.shortcuts import render
from django.views import  View
from student.models import StudentName
class indexView(View):
    def get(self,request):
        stundet_count = StudentName.objects.all().count()
        return render(request,"test.html",{
            "stundet_count":stundet_count
        })