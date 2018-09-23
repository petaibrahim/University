from django.urls import reverse_lazy,reverse
from django.views import generic
from django.views.generic import ListView,TemplateView
from django.views.generic.edit import CreateView, UpdateView
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django_tables2 import RequestConfig
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserChangeForm, UserForm, TeacherForm, StudentResultForm
from .tables import *
from django.db.models import Avg


class Login(generic.CreateView):
    form_class = CustomUserChangeForm
    success_url = reverse_lazy('index')
    template_name = 'Dashboard/login.html'

@method_decorator(login_required, name='dispatch')
class IndexView(ListView):
    template_name = 'Dashboard/index.html'

    def get_queryset(self):
        return Course.objects.all()

@method_decorator(login_required, name='dispatch')
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
            )
        return HttpResponseRedirect(self.get_success_url())

@login_required
def course(request):
    table = CourseTable(Course.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'Dashboard/course.html', {'table': table})

@login_required
def teacher(request):
    table = TeacherTable(Teacher.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'Dashboard/teacher.html', {'table' : table})

@login_required
def student(request):
    table = StudentTable(Student.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'Dashboard/student.html', {'table' : table})

@login_required
def result(request):
    table = ResultTable(Result.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'Dashboard/result.html', {'table' : table})

@login_required
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = TeacherForm(request.POST,request.FILES, instance=request.user.teacher)
        if user_form.is_valid() and profile_form.is_valid():

            user_form.save()
            profile_form.save()
            messages.success(request,('Your profile was successfully updated!'), extra_tags='alert')
            return redirect('Dashboard:profile')
        else:
            messages.error(request, ('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = TeacherForm(instance=request.user.teacher)
    return render(request, 'Dashboard/updateProfile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

@method_decorator(login_required, name='dispatch')
class FindStudent(ListView):
    template_name = 'Dashboard/findStudent.html'
    model = Student
    fields = ['sbtc']

    def get_queryset(self):
        batch = Student.objects.values_list('sbtc').distinct()
        return batch

@method_decorator(login_required, name='dispatch')
class FindStudentdetail(ListView):
    template_name = 'Dashboard/findStudentdetail.html'
    model = Student
    fields = ['all']

    def get_queryset(self):
        student = Student.objects.filter(sbtc=self.kwargs['pk'])
        return student

@method_decorator(login_required, name='dispatch')
class FindStudentresult(ListView):
    template_name = 'Dashboard/findStudentresult.html'
    model = Result
    fields = ['all']

    def get_queryset(self):
        result=Result.objects.filter(student=self.kwargs['pk1'])
        return result

class UpdateStudent(UpdateView):
    model = Result
    template_name = 'Dashboard/updatestudent.html'
    form_class =StudentResultForm

    def get_object(self):
        result = Result.objects.filter(id=self.kwargs['pk3'])
        return get_object_or_404(result)

    # def get_success_url(FindStudentresult):
    #     return reverse_lazy('Dashboard:findstudentdetail', kwargs={'pk': FindStudentresult.kwargs['pk']})


    def get_success_url(FindStudentresult):
        return reverse_lazy('Dashboard:findstudent')


@method_decorator(login_required, name='dispatch')
class SelectSession(ListView):
    template_name = 'Dashboard/selectsession.html'
    model = Session
    fields = ['sesid']

    def get_queryset(self):
        return Session.objects.all()

@method_decorator(login_required, name='dispatch')
class SelectCourse(ListView):
    template_name = 'Dashboard/selectcourse.html'
    model = Registration
    fields = ['all']

    def get_queryset(self):
        course = Registration.objects.filter(session_id=self.kwargs['session_pk'])
        return course

@method_decorator(login_required, name='dispatch')
class BatchResult(ListView):
    template_name = 'Dashboard/batchResult.html'
    model = Result
    fields = ['all']

    def get_queryset(self):
        result=Result.objects.filter(asign__reg_id=self.kwargs['pk_1'])
        return result


