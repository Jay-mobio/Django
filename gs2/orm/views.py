from django.shortcuts import render
from orm.models import Student

# Create your views here.
def Studentinfo(request):
    stud = Student.objects.all()
    return render(request,'studentdetails.html',{'stu': stud})
