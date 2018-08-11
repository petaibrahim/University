from django.urls import path
from . import views

app_name = 'Dashboard'

urlpatterns = [
    path('registration:login', views.Login.as_view(), name='login'),
    path('', views.IndexView.as_view(), name='index'),
    path('course/', views.course, name='course'),
    path('teacher/', views.teacher, name='teacher'),
    path('student/', views.student, name='student'),
    path('result/', views.result, name='result'),
    path('CreateSession/', views.SessionView.as_view(), name='session'),

]

