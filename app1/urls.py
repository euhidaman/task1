from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('logindisplay/', views.logindisplay, name='logindisplay'),
    path('about/', views.about, name='about'),
    path('hyper/',views.hyper,name='hyper'),
    path('selectdate/',views.selectdate,name='date_select'),
    path('dateoutput/',views.dateprint,name='date_print'),
    path('add/',views.add,name='addition_start'),
    path('addition/',views.addition,name='addition'),
    path('op/',views.op,name='op_start'),
    path('expression/',views.expression,name='op_end'),
    path('great/',views.great,name='great_start'),
    path('greater/',views.greater,name='great_end'),
    path('greatagain/',views.greatagain,name='greathree_start'),
    path('greaterthree/',views.greaterthree,name='greathree_end'),
    path('primestart/',views.primestart,name='prime_start'),
    path('primeend/',views.prime_cal,name='prime_end'),
    path('collegesignup/',views.clgsignup,name='college_signup'),
    path('collegedisplay/',views.clgdisplay,name='college_display'),
]
