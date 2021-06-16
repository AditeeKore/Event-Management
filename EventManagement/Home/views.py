from django.shortcuts import render, HttpResponse
from datetime import datetime
from Home.models import sign_up

# Create your views here.
def home(request):
    return render(request, 'home.html')
    #return HttpResponse('This is a Home page')

def about(request):
    return render(request, 'about.html')
    #return HttpResponse('This is a about page')

def userlogin(request):
    return render(request, 'userlogin.html')
    #return HttpResponse('This is a userlogin page')

def registration_form(request):
    return render(request, 'registration_form.html')
    #return HttpResponse('This is a registration_form page')

def sign_up(request):
    if request.method == "POST":
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        email=request.POST.get('email')
        password=request.POST.get('password')
        Signup= sign_up(fname= fname,lname=lname, email=email, password=password, date=datetime.today())
        Signup.save()
    return render(request, 'sign_up.html')
    #return HttpResponse('This is a sign_up page')

def party(request):
    return render(request, 'party.html')
    #return HttpResponse('This is a party page')

def conference(request):
    return render(request, 'conference.html')
    #return HttpResponse('This is a conference page')

def online(request):
    return render(request, 'online.html')
    #return HttpResponse('This is a online page')

def theatre(request):
    return render(request, 'theatre.html')
    #return HttpResponse('This is a theatre page')

def sports(request):
    return render(request, 'sports.html')
    #return HttpResponse('This is a sports page')