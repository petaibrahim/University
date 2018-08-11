from django import forms
from django.contrib.auth.forms import UserChangeForm
from .models import Teacher


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = Teacher
        fields = ('user','full_name')



