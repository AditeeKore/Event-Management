from django.contrib import admin
from Home.models import Registration, sign_up, userlogin

# Register your models here.
admin.site.register(sign_up)
admin.site.register(Registration)
admin.site.register(userlogin)
