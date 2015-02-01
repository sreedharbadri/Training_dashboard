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
        #new = Course.objects.get(name=request.POST['course'])
        #new1 = Enquiry.objects.get(enquiry_type=request.POST['enquiry'])
        #Fcourse = str(new.name)
        Student.objects.create(name=request.POST['student_name'],
                               phone=request.POST['phone'],
                               course=request.POST['course'],
                               enquiry=request.POST['enquiry'],
                               #new.student_set.create(course=request.POST['course']),
                               #new1.student_set.create(enquiry_type=request.POST['enquiry']),
                               doj=request.POST['doj'],

        )
        return redirect ('/hello/')
    else:
        form=StudentForm
        context={'form':form}
        return render(request,'form1.html',context)
