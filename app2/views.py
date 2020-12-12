from django.shortcuts import render
from django.http import HttpResponse
from app2.models import student

def signup(request):
    return render(request, 'task1/signup.html')

def signupdisplay(request):
    first_name = request.POST['firstname']
    last_name = request.POST['lastname']
    useremail = request.POST['useremail']
    x = student.objects.create(firstname = first_name, lastname = last_name, email = useremail)
    x.save()
    return render(request, 'task1/a.html')
