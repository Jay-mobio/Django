from django.shortcuts import render
from .forms import StudentRegistrartion

# Create your views here.
def showformdata(request):
    fm = StudentRegistrartion(label_suffix=':',initial={'uname':'user-name','password':'password','email':'email'})
    return render(request,'form/userregestration.html',{'form':fm})