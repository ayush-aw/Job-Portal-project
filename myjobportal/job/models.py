from django.db import models

# Create your models here.
class JOBS(models.Model):

    POSTEDCHOICE=(('company','COMPANY'),('consultant','CONSULTANT'),('admin','ADMIN'),)
    statuschoice=(('open','OPEN'),('close','CLOSE'),('select','SELECT'),)
    typechoice=(('full time','FULL TIME'),('part time','PART TIME'),('select','SELECT'),)
    POSTEDBY=models.CharField(max_length=20,choices=POSTEDCHOICE,default='admin')
    COMPANY=models.CharField(max_length=500)
    LOCATION = models.CharField(max_length=900)
    POST=models.CharField(max_length=100)
    MINIMUMEXPERIENCE=models.CharField(max_length=120)
    MINIMUMQUALIFICATION=models.CharField(max_length=120)
    SALARYRANGE=models.CharField(max_length=100)
    JOBDESCRIPTION=models.TextField(max_length=1000)
    CONTACTPERSON=models.CharField(max_length=100)
    MOBILE=models.CharField(max_length=20)
    POSTDATE=models.DateField()
    CURRENTSTATUS=models.CharField(max_length=30,choices=statuschoice,default='select')
    EMPLOYMENTTYPE=models.CharField(max_length=30,choices=typechoice,default='select')
    def __str__(self):
        return self.COMPANY

class CANDIDATE(models.Model):
    NAME=models.CharField(max_length=40)
    MOBILENUMBER=models.CharField(max_length=20)
    EMAILID=models.EmailField()
    CREATEPASSWORD=models.CharField(max_length=20)
    ADDRESS=models.CharField(max_length=200)
    JOBINTERESTED=models.CharField(max_length=50)
    QULIFICATION=models.CharField(max_length=20)
    EXPERIENCE=models.CharField(max_length=10)
    EXPECTEDSALARY=models.CharField(max_length=30)
    CURRENTLOCATION=models.TextField()
    PREFEREDLOCATION=models.TextField()
    RESUME=models.TextField()
    def __str__(self):
        return self.NAME

class COMPANY(models.Model):
    COMPANYNAME=models.CharField(max_length=100)
    ADDRESS=models.CharField(max_length=200)
    CREATEPASSWORD = models.CharField(max_length=20)
    STATE=models.CharField(max_length=50)
    PINCODE=models.CharField(max_length=10)
    COUNTRY=models.CharField(max_length=20)
    EMAILID=models.EmailField()
    LANDLINENUMBER=models.IntegerField()
    MOBILENUMBER=models.IntegerField()
    SECTOR=models.CharField(max_length=50)
    def __str__(self):
        return self.COMPANYNAME


class CONSULTANT(models.Model):
    CONSULTANTNAME=models.CharField(max_length=100)
    ADDRESS=models.CharField(max_length=200)
    CREATEPASSWORD = models.CharField(max_length=20)
    STATE=models.CharField(max_length=50)
    PINCODE=models.CharField(max_length=10)
    COUNTRY=models.CharField(max_length=20)
    EMAILID=models.EmailField()
    LANDLINENUMBER=models.IntegerField()
    MOBILENUMBER=models.IntegerField()
    SECTOR=models.CharField(max_length=50)
    def __str__(self):
        return self.CONSULTANTNAME


class login(models.Model):
    name=models.CharField(max_length=10)
    password=models.CharField(max_length=20)
    def __str__(self):
        return self.name

class applyjob(models.Model):
    NAME=models.CharField(max_length=30)
    MOBILE=models.CharField(max_length=15)
    EMAIL=models.EmailField()
    RESUME=models.TextField()
    def __str__(self):
        return self.NAME