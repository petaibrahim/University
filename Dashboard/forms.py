from django import forms
from django.contrib.auth.forms import UserChangeForm
from .models import Teacher, Result
from django.contrib.auth.models import User


class CustomUserChangeForm(UserChangeForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = Teacher
        fields = ('user',)

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ( 'username', 'first_name', 'last_name', 'email')

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ('user','mobile','avatar')


class StudentResultForm(forms.ModelForm):
    class Meta:
        model = Result
        fields = ('ct1', 'ct2', 'ct3', 'ct4', 'asn')

# class FindStudentForm(forms.ModelForm):
#     class Meta:
#         model = Student
#         fields = ('sbtc',)
# class ContactForm(forms.ModelForm):
#     class Meta:
#         model = Student
#         fields = ('sbtc',)





