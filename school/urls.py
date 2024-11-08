from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='school'),
    path('studentsignin', views.studentsignin, name='studentsignin'),
    path('teachersignin', views.teachersignin, name='teachersignin'),
    path('studentsignup', views.studentsignup, name='studentsignup'),
    path('teachersignup', views.teachersignup, name='teachersignup'),
    path('studentportal', views.studentportal, name='studentportal'),
    path('teacherportal', views.teacherportal, name='teacherportal'),
    path('studentresultcard', views.studentresultcard, name='studentresultcard'),
    path('changeresult/<int:rollno>', views.changeresult, name='changeresult'),
    path('addnewstd', views.addnewstd, name='changeresult'),
    path('viewresult/<int:rollno>', views.viewresult, name='changeresult'),
]