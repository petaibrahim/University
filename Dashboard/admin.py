from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserChangeForm
from .models import *

class CustomUserAdmin(UserAdmin):
    form = CustomUserChangeForm
    model = Teacher
    list_display = ['user']


admin.site.register(Course)
admin.site.register(Session)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Registration)
admin.site.register(Result)

