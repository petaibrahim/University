from django.urls import path
from . import views
from .forms import CustomUserChangeForm
app_name = 'Dashboard'


urlpatterns = [
    path('login', views.Login.as_view(),{'authentication_form':CustomUserChangeForm},name='login'),
    path('', views.IndexView.as_view(), name='index'),
    path('course/', views.course, name='course'),
    path('teacher/', views.teacher, name='teacher'),
    path('student/', views.student, name='student'),
    path('result/', views.result, name='result'),
    path('profile/', views.update_profile, name='profile'),

    path('selectsession/', views.SelectSession.as_view(), name='selectsession'),
    path('selectsession/<int:session_pk>/', views.SelectCourse.as_view(), name='selectcourse'),
    path('selectsession/<int:session_pk>/<int:pk_1>', views.BatchResult.as_view(), name='selectresult'),

    path('findstudent/', views.FindStudent.as_view(), name='findstudent'),
    path('findstudent/<int:pk>/', views.FindStudentdetail.as_view(), name='findstudentdetail'),
    path('findstudent/<int:pk>/<int:pk1>/', views.FindStudentresult.as_view(), name='findstudentresult'),
    path('findstudent/<int:pk>/<int:pk1>/edit<int:pk3>/', views.UpdateStudent.as_view(), name='editstudent'),

    path('session/', views.SessionView.as_view(success_url="Dasboard:session"), name='session'),
]

