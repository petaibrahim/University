from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.http import HttpResponseRedirect

from django.shortcuts import render, redirect
from django_tables2 import RequestConfig
from .tables import *
from .models import *


from .forms import CustomUserChangeForm



class Login(generic.CreateView):
    form_class = CustomUserChangeForm
    success_url = reverse_lazy('index')
    template_name = 'Dashboard/login.html'

class IndexView(ListView):
    template_name = 'Dashboard/index.html'

    def get_queryset(self):
        return Course.objects.all()

def course(request):
    table = CourseTable(Course.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'Dashboard/course.html', {'table': table})

def teacher(request):
    table = TeacherTable(Teacher.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'Dashboard/teacher.html', {'table' : table})

def student(request):
    table = StudentTable(Student.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'Dashboard/student.html', {'table' : table})

def result(request):
    table = ResultTable(Result.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'Dashboard/result.html', {'table' : table})



class SessionView(CreateView,ListView):
    template_name = 'Dashboard/createSession.html'
    model = Session
    fields = ['sesid']

    def get_queryset(self):
        return Session.objects.all()

    def form_valid(self, form):  # this will be the creation form
        instance = form.save()  # save the empty session
        for course in Course.objects.all():
            assert isinstance(course, object)
            Registration.objects.create(
                session=instance,
                course=course,
                # teacher=self.request.user.teacher,  # (Is this correct?)
            )
            return redirect('Dashboard:session')





















