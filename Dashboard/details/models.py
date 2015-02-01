from django.db import models

# Create your models here.
class Course(models.Model):
    name=models.CharField(max_length=250, primary_key=True)
    def __unicode__(self):
        return self.name

class Enquiry(models.Model):
    enquiry_type=models.CharField(max_length=250, primary_key=True)
    def __unicode__(self):
        return self.enquiry_type

class Status(models.Model):
    status_info=models.CharField(max_length=250, primary_key=True)
    def __unicode__(self):
        return self.status_info

class Student(models.Model):
    name=models.CharField(max_length=250)
    phone=models.CharField(max_length=250, primary_key=True)
    course=models.ForeignKey(Course)
    enquiry=models.ForeignKey(Enquiry)
    doj=models.DateField()
