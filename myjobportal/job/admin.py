from django.contrib import admin
from .models import JOBS,CANDIDATE,COMPANY,CONSULTANT,applyjob
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('POSTEDBY', 'COMPANY', 'LOCATION', 'POST', 'MINIMUMEXPERIENCE','MINIMUMQUALIFICATION','SALARYRANGE','JOBDESCRIPTION','CONTACTPERSON','MOBILE','POSTDATE','CURRENTSTATUS','EMPLOYMENTTYPE')
    list_filter = ('POSTEDBY', 'COMPANY', 'LOCATION', 'POST')
    search_fields = ('COMPANY', 'LOCATION','POST')
admin.site.register(JOBS, PostAdmin)
class PostAdmin(admin.ModelAdmin):
    list_display = ('NAME', 'MOBILENUMBER', 'EMAILID', 'CREATEPASSWORD', 'ADDRESS','JOBINTERESTED','QULIFICATION','EXPERIENCE','EXPECTEDSALARY','CURRENTLOCATION','PREFEREDLOCATION','RESUME')
    list_filter = ('NAME', 'QULIFICATION')
    search_fields = ('NAME',)
admin.site.register(CANDIDATE, PostAdmin)
class PostAdmin(admin.ModelAdmin):
    list_display = ('COMPANYNAME', 'ADDRESS', 'STATE', 'PINCODE', 'COUNTRY','EMAILID','LANDLINENUMBER','MOBILENUMBER','SECTOR')
    list_filter = ('COMPANYNAME', 'COUNTRY')
    search_fields = ('COMPANYNAME', 'COUNTRY')
admin.site.register(COMPANY, PostAdmin)
class PostAdmin(admin.ModelAdmin):
    list_display = ('CONSULTANTNAME', 'ADDRESS', 'STATE', 'PINCODE', 'COUNTRY','EMAILID','LANDLINENUMBER','MOBILENUMBER','SECTOR')
    list_filter = ('CONSULTANTNAME', 'COUNTRY')
    search_fields = ('CONSULTANTNAME', 'COUNTRY')
admin.site.register(CONSULTANT, PostAdmin)
admin.site.register(applyjob)

admin.site.site_header="Job Portal Administration"