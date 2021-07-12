from django.db import models

# Create your models here.
class sign_up(models.Model):
    username=models.CharField(max_length=50, default='SOME STRING')
    fname =models.CharField(max_length=20)
    lname=models.CharField(max_length=20)
    email=models.EmailField(max_length=50)
    password=models.CharField(max_length=25)
    date=models.DateField()

    def __str__(self):
        return self.username

class Registration(models.Model):
    name=models.CharField(max_length=50)
    phone=models.CharField(max_length=12)
    email=models.EmailField(max_length=50)
    eventname=models.CharField(max_length=50)
    eventtype=models.CharField(max_length=30)
    eventlocation=models.CharField(max_length=100)
    guestlimit=models.CharField(max_length=10)
    date=models.DateField()
    time=models.TimeField()
    fee=models.CharField(max_length=6)
    disc=models.CharField(max_length=1000)

    def __str__(self):
        return self.name

class userlogin(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=25)

    def __str__(self):
        return self.username


