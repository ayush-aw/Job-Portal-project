from django.urls import path
from . import views
urlpatterns=[
    path('',views.index,name='index'),
    path('jobs/',views.jobs,name='jobs'),
    path('<int:job_id>/',views.detail,name='detail'),
    path('post/',views.post,name='post'),
    path('addpost/',views.addpost,name='addpost'),
    path('contact/',views.contact,name='contact'),
    path('upload/',views.reg,name='reg'),
    path('addcondidate/',views.addcondidate,name='addcondidate'),
    path('addcompany/',views.addcompany,name='addcompany'),
    path('addconsultant',views.addconsultant,name='addconsultant'),
    path('login/',views.login,name='login'),
    path('log/',views.log,name='log'),
    path('apply',views.apply,name='apply'),
    path('appforjob',views.appforjob,name='appforjob'),
]