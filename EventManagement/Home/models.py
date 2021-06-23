from django.db import models

# Create your models here.
class Signup(models.Model):
    fname =models.CharField(max_length=20)
    lname=models.CharField(max_length=20)
    email=models.EmailField(max_length=50)
    password=models.CharField(max_length=25)
    date=models.DateField()

    def __str__(self):
        return self.fname



