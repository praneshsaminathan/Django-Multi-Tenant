from django.contrib import admin

# Register your models here.
from .models import *

# @admin.register(MyUser)
# class MyUserAdmin(admin.ModelAdmin):
#     pass

admin.site.register(MyUser)