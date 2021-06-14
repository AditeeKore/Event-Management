from django.contrib import admin
from django.urls import path
from Home import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('about', views.about, name='about'),
    path('userlogin', views.userlogin, name='userlogin'),
    path('registration_form', views.registration_form, name='registration_form'),
    path('sign_up', views.sign_up, name='sign_up'),
    path('party', views.party, name='party'),
    path('conference', views.conference, name='conference'),
    path('online', views.online, name='online'),
    path('sports', views.sports, name='sports'),
    path('theatre', views.theatre, name='theatre'),
]

