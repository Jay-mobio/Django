from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    data = {
        'title':'New Home',
        "bdata" : 'Welcome to bdata',
        'clist': ['php','java','Django'],
        'numbers':[10,20,30,40,50],
        'student_details': {
            'name':'pradeep','phone':7894561230,
            'name':'robin','phone':1234567890
        }
    }
    return render(request,'index.html',data)
def aboutUs(request):
    return HttpResponse("Welcome to wscubetech")

def Course(request):
    return HttpResponse("Welcome to wscubetech!!!!")

def CourseDetails(request,courseid):
    return HttpResponse(courseid)