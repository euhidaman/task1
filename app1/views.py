from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'task1/a.html')

def login(request):
    return render(request, 'task1/login.html')

def logindisplay(request):
    fname = request.POST['firstname']
    lname = request.POST['lastname']
    mail = request.POST['useremail']
    gen = request.POST['gender']
    city = request.POST['city']
    country = request.POST['country']
    pword = request.POST['password']
    age = request.POST['ageverification']
    citizen = request.POST['citizen']
    return render(request, 'task1/logindisplay.html', {'fname': fname,'lname': lname,'mail':mail, 'gen':gen, 'city':city, 'country':country, 'pword':pword, 'age':age, 'citizen':citizen})

def clgsignup(request):
    return render(request, 'task1/collegesignup.html')

def clgdisplay(request):
    stuname = request.POST['studentname']
    fa_name = request.POST['fathername']
    fa_occ = request.POST['fatheroccupation']
    addr = request.POST['address']
    high_edu = request.POST['higheredu']
    dob = request.POST['birthday']
    emailid = request.POST['email']
    phoneno = request.POST['txtEmpPhone']
    gen = request.POST['gender']
    branches = request.POST.getlist('branch[]',[])
    return render(request, 'task1/clgsignupdisplay.html', {'stuname': stuname, 'fa_name':fa_name, 'fa_occ': fa_occ, 'addr':addr, 'high_edu':high_edu, 'dob':dob, 'emailid':emailid, 'phoneno':phoneno,'gen':gen, 'branches':branches})


def about(request):
    return render(request, 'task1/about.html')

def hyper(request):
    return render(request, 'task1/youtube.html', {'address': 'https://www.youtube.com/'})

def selectdate(request):
    return render(request, 'task1/date.html')

def dateprint(request):
    da = request.GET['date1']
    return render(request, 'task1/dateop.html', {'Date':da})

def add(request):
    return render(request, 'task1/add.html')

def addition(request):
    val1 = int(request.POST['num1'])
    val2 = int(request.POST['num2'])
    res = val1 + val2
    return render(request, 'task1/addans.html', {'Answer': res})

def op(request):
    return render(request, 'task1/oper.html')

def expression(request):
    val1 = int(request.POST['num1'])
    val2 = int(request.POST['num2'])
    oper = request.POST['op']

    if (oper == 'add'):
        res = val1 + val2
    elif (oper == 'sub'):
        res = val1 - val2
    elif (oper == 'mul'):
        res = val1*val2
    elif (oper == 'div'):
        res = val1/val2
    else:
        res = "NOT Answered"
    return render(request, 'task1/oper.html', {'res': res})

def great(request):
    return render(request, 'task1/greatwo.html')

def greater(request):
    val1 = int(request.POST['num1'])
    val2 = int(request.POST['num2'])
    if (val1 > val2):
        res = ("{} is greater than {}".format(val1,val2))
    elif (val1 < val2):
        res = ("{} is greater than {}".format(val2,val1))
    elif (val1 == val2):
        res = ("{} is equal to {}".format(val1,val2))
    else:
        res = "Unable to Solve"
    return render(request, 'task1/greatwo.html', {'res': res})

def greatagain(request):
    return render(request, 'task1/greathree.html')

def greaterthree(request):
    a = int(request.POST['num1'])
    b = int(request.POST['num2'])
    c = int(request.POST['num3'])

    if a > b and a > c:
        res = ("Maximum is {}".format(a))
    elif b > c and b > a:
       res = ("Maximum is {}".format(b))
    elif c > a and c > b:
       res = ("Maximum is {}".format(c))
    else:
       res = "Unable to solve"

    return render(request, 'task1/greathree.html', {'res': res})

def primestart(request):
    return render(request, "task1/prime.html")

def prime_cal(request):
    a = int(request.POST['num1'])

    if a>1:
        for i in range(2, a):
            if ((a%i)==0) :
                res = ("{} is not prime".format(a))
                break
            else:
                res = ("{} is prime".format(a))
        else:
            res = ("{} is prime".format(a))
    else:
        res = ("{} is not prime".format(a))
    return render(request, 'task1/prime.html', {'res': res})
