from django.shortcuts import render

# Create your views here.

from django.shortcuts import render,redirect
from details.models import Course,Enquiry,Status,Student
from details.form import StudentForm
# Create your views here.

def contacts_hello(request):
    values=Student.objects.all()
    context={'namesdb':values}
    return render(request,"hello.html",context)

def Student_Form(request):
    if request.method == 'POST':
        Student.objects.create(name=request.POST['student_name'],
                               phone=request.POST['phone'],
                               course=Course.objects.get(name=request.POST['course']),
                       # Notes: Student(field) = <database>.objects.get(<database_field>=request.POST['<form field>']
                               enquiry=Enquiry.objects.get(enquiry_type=request.POST['enquiry']),
                               doj=request.POST['doj']


        )
        return redirect ('/contacts_hello/')
    else:
        form=StudentForm
        context={'form':form}
        return render(request,'form1.html',context)
