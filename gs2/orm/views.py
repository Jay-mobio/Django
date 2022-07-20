from django.shortcuts import render
from orm.models import Student

# Create your views here.
def Studentinfo(request):
    
    stud1 = Student.objects.create(stuname='jay',stuid='105',stuemail='1243@email.com',stupass='41234')
    stud1.save()
    stud2 = Student.objects.create(stuname='jay1',stuid='1051',stuemail='1243@email.com1',stupass='412341')
    stud2.save()
    stud3 = Student.objects.create(stuname='jay2',stuid='1052',stuemail='1243@email.com2',stupass='412342')
    stud3.save()
    stud = [stud1,stud2,stud3]
    # stud = Student.objects.all()
    
    stud = Student.objects.filter(stuid='105')
    # stud = Student.objects.filter(stuname='Rahul', stuid='3').values()

    return render(request,'studentdetails.html',{'stu': stud})


