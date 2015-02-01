from django import forms


class StudentForm(forms.Form):
    student_name=forms.CharField(label='NAME')
    phone=forms.CharField(label='PHONE NUMBER')
    course=forms.CharField(label='COURSE')
    enquiry=forms.CharField(label='ENQUIRY')
    doj=forms.CharField(label='DATE OF JOIN')
