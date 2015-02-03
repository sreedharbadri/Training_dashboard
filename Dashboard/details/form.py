from django import forms
from details.models import Enquiry,Course


class StudentForm(forms.Form):
    student_name=forms.CharField(label='NAME')
    phone=forms.CharField(label='PHONE NUMBER')
    course=forms.ModelMultipleChoiceField(queryset=Course.objects.all())
    enquiry=forms.ModelMultipleChoiceField(queryset=Enquiry.objects.all())
    doj=forms.CharField(label='DATE OF JOIN')
