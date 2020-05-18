from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.models import User
from django.contrib import auth
from .models import login,applyjob

from .models import JOBS,CANDIDATE,COMPANY,CONSULTANT
# Create your views here.
def index(request):
    job=JOBS.objects.order_by('-POSTDATE')[:10]
    context={'job':job}
    return render(request,'job/index.html',context)
def jobs(request):
    job = JOBS.objects.order_by('-POSTDATE')[:10]
    context = {'job': job}
    return render(request,'job/jobs.html',context)
def detail(request,job_id):
    data=get_object_or_404(JOBS,pk=job_id)
    return render(request,'job/detail.html',{'data':data})
def post(request):
    return render(request,'job/post.html')
def addpost(request):
    print("form submited")
    postedby=request.POST["postedby"]
    Company = request.POST["Company"]
    Location = request.POST["Location"]
    Post = request.POST["Post"]
    Experience = request.POST["Experience"]
    Qulification = request.POST["Qulification"]
    Salary = request.POST["Salary"]
    Description = request.POST["Description"]
    Contact = request.POST["Contact"]
    mobile = request.POST["mobile"]
    Postdate = request.POST["Postdate"]
    status = request.POST["status"]
    type = request.POST["type"]
    postinfo=JOBS(POSTEDBY=postedby,COMPANY=Company,LOCATION=Location,POST=Post,MINIMUMEXPERIENCE=Experience,MINIMUMQUALIFICATION=Qulification,SALARYRANGE=Salary,JOBDESCRIPTION=Description,CONTACTPERSON=Cont77act,MOBILE=mobile,POSTDATE=Postdate,CURRENTSTATUS=status,EMPLOYMENTTYPE=type)
    postinfo.save()
    return render(request,'job/post.html')
def contact(request):
    return render(request,'job/contact.html')

def reg(request):
    return render(request,'job/upload.html')
def addcondidate(request):
    Name=request.POST["name"]
    Mobile=request.POST["mobile"]
    Email=request.POST["email"]
    Crpass=request.POST["Password"]
    Add=request.POST["Address"]
    Jobint=request.POST["Job"]
    Qulif=request.POST["Qulification"]
    Exp=request.POST["Experience"]
    Expec=request.POST["Salary"]
    Crloc=request.POST["Currlocation"]
    Preloc=request.POST["Prelocation"]
    Res=request.POST["Res"]
    condidateinfo=CANDIDATE(NAME=Name,MOBILENUMBER=Mobile,EMAILID=Email,CREATEPASSWORD=Crpass, ADDRESS=Add,JOBINTERESTED=Jobint,QULIFICATION=Qulif,EXPERIENCE=Exp,EXPECTEDSALARY=Expec,CURRENTLOCATION=Crloc, PREFEREDLOCATION=Preloc,RESUME=Res)
    user = User(username=Name, password=Crpass,is_staff=True)
    user.save()
    condidateinfo.save()
    return render(request,'job/upload.html')
def addcompany(request):
    Comname=request.POST["name"]
    Add=request.POST["Address"]
    Crpass = request.POST["Password"]
    Sta=request.POST["State"]
    Pin=request.POST["Pincode"]
    Con=request.POST["Country"]
    Em=request.POST["email"]
    Land=request.POST["Landline"]
    Mobile=request.POST["mobile"]
    Sec=request.POST["Sector"]
    companyinfo=COMPANY(COMPANYNAME=Comname,ADDRESS=Add,CREATEPASSWORD=Crpass,STATE=Sta,PINCODE=Pin,COUNTRY=Con,EMAILID=Em,LANDLINENUMBER=Land,MOBILENUMBER=Mobile,SECTOR=Sec)
    companyinfo.save()
    user = User(username=Comname, password=Crpass)
    user.save()
    return render(request, 'job/upload.html')
def addconsultant(request):
    Conname=request.POST["name"]
    Add=request.POST["Address"]
    Crpass = request.POST["Password"]
    Sta=request.POST["State"]
    Pin=request.POST["Pincode"]
    Con=request.POST["Country"]
    Em=request.POST["email"]
    Land=request.POST["Landline"]
    Mobile=request.POST["mobile"]
    Sec=request.POST["Sector"]
    companyinfo=CONSULTANT(CONSULTANTNAME=Conname,ADDRESS=Add,CREATEPASSWORD=Crpass,STATE=Sta,PINCODE=Pin,COUNTRY=Con,EMAILID=Em,LANDLINENUMBER=Land,MOBILENUMBER=Mobile,SECTOR=Sec)
    companyinfo.save()
    user = User(username=Conname, password=Crpass)
    user.save()
    return render(request, 'job/upload.html')
def login(request):
    return render(request,'job/login.html')
def log(request):
    if request.method=="POST":
        username=request.POST['name']
        password=request.POST['pass']

        user=auth.authenticate(username=username,password=password)
        if user is not None:
                auth.login(request,user)
                return render(request,'job/index.html')
        else:
          return render(request,'job/upload.html')
#def logout(request):
    #auth.logout(request)
    #return HttpResponseRedirect('logout.html')
def apply(request):
    return render(request,'job/apply.html')


def appforjob(request):
    if request.method=="POST":
        Name=request.POST['name']
        Mobile=request.POST['mobile']
        Email=request.POST['email']
        Cv=request.POST['cv']
        appinfo=applyjob(NAME=Name,MOBILE=Mobile,EMAIL=Email,RESUME=Cv)
        appinfo.save()
        return render(request,'job/apply.html')
