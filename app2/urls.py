from django.urls import path
from . import views

urlpatterns = [
    path('', views.signup, name='signup'),
    # any path started from here , for example in forms will have action such as 'signup/action_part'
    path('signupdisplay/', views.signupdisplay, name='signupdisplay'),
]
