import django_tables2 as tables
from .models import *

class TeacherTable(tables.Table):
    class Meta:
        model = Teacher
        template_name = 'django_tables2/bootstrap-responsive.html'
        sequence = ('full_name', 'umob')
        exclude = ('id', 'user')
        ulogo = tables.TemplateColumn('<img src="{{Teacher.ulogo.url}}"> ')

class CourseTable(tables.Table):
    class Meta:
        model = Course
        template_name = 'django_tables2/bootstrap-responsive.html'
        sequence = ('cidn','cnam','cred')
        exclude = ('cid')

class StudentTable(tables.Table):
    class Meta:
        model = Student
        template_name = 'django_tables2/bootstrap-responsive.html'
        sequence = ('sroll','snam','sreg','sbtc', 'sses')
        exclude = ('sid')

class ResultTable(tables.Table):
    class Meta:
        model = Result
        template_name = 'django_tables2/bootstrap-responsive.html'
        # sequence = ('sroll','snam','sreg','sbtc', 'sses')
        # exclude = ('sid')