from django.contrib import auth
from EventManagement.settings import AUTH_PASSWORD_VALIDATORS
from django.shortcuts import redirect, render, HttpResponse
from datetime import datetime
from Home.models import sign_up, Registration, userlogin
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


# Create your views here.
def home(request):
    return render(request, 'home.html')
    #return HttpResponse('This is a Home page')

def about(request):
    return render(request, 'about.html')
    #return HttpResponse('This is a about page')

def userlogin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")

    form = AuthenticationForm()
    return render(request = request,
                  template_name = "userlogin.html",
                  context={"form":form})
    # if request.method == "POST":
    #     email=request.POST.get('email')
    #     password=request.POST.get('password')

    #     user = authenticate(email=email, password=password)

    #     if user is not None:
    #         auth.userlogin(request, user)
    #         return redirect("/")

    #     else:
    #         messages.info(request, 'Invalid Credentials')
    #         return redirect('userlogin.html')
    # return render(request, 'userlogin.html')
    # #return HttpResponse('This is a userlogin page')

def registration_form(request):
    if request.method == "POST":
        name=request.POST.get('name')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        eventname=request.POST.get('eventname')
        eventtype=request.POST.get('eventtype')
        eventlocation=request.POST.get('eventlocation')
        date=request.POST.get('date')
        time=request.POST.get('time')
        guestlimit=request.POST.get('guestlimit')
        disc=request.POST.get('disc')
        registration_form=Registration(name=name, phone=phone, email=email, eventname=eventname, 
        eventtype=eventtype, eventlocation=eventlocation, date=date, time=time, guestlimit=guestlimit, disc=disc)
        registration_form.save()
        messages.success(request, 'Congratulations!! Your have successfully registered your event.')
    return render(request, 'registration_form.html')
    #return HttpResponse('This is a registration_form page')

def sign_up(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            userlogin(request, user)
            return redirect("home.html")
        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])

    form = UserCreationForm
    return render(request = request,
                  template_name = "sign_up.html",
                  context={"form":form})
    # if request.method == "POST":
    #     fname=request.POST.get('fname')
    #     lname=request.POST.get('lname')
    #     email=request.POST.get('email')
    #     password=request.POST.get('password')

    #     if Signup.objects.filter(email=email).exists():
    #         print('Email already taken')
    #     else:
    #         sign_up=Signup(fname= fname,lname=lname, email=email, password=password, date=datetime.today())
    #         sign_up.save()
    #         messages.success(request, 'Congratulations!! Your have successfully signed up.')
    # return render(request, 'sign_up.html')
    # #return HttpResponse('This is a sign_up page')

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