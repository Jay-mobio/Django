from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def learn_django(request):
    coursename = {
        'cname':'django',
    }
    return render(request,'course/courseone.html',coursename)

def learn_python(request):
    return render(request,'course/coursetwo.html')
    
def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html', )

def core(request):
    return render(request,'core.html')
