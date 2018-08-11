from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Course(models.Model):
    cid = models.AutoField(primary_key=True)
    cnam = models.CharField(max_length=200)
    cidn = models.IntegerField()
    cred = models.IntegerField()

    def __str__(self):
        return 'IT-' + str(self.cidn) + ' - ' + self.cnam

class Student(models.Model):
    snam = models.CharField(max_length=200)
    sid = models.AutoField(primary_key=True)
    sroll = models.IntegerField()
    sreg = models.IntegerField()
    sbtc = models.IntegerField()
    sses = models.CharField(max_length=10)

    def __str__(self):
        return self.snam

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200, null=True)
    umob = models.CharField(max_length=20, blank=True, default='')
    ulogo = models.ImageField(upload_to='media', blank=True)

    def __str__(self):
        return self.user.username

    def createprofile(selfsender, **kwargs):
        if kwargs['created']:
            user_profile = Teacher.objects.creeate(user=kwargs['instance'])

class Session(models.Model):
    sesid = models.IntegerField(primary_key=True,verbose_name= ('Session'))

    def __str__(self):
        return str(self.sesid)
    def get_absolute_url(self):
        return reverse('Dashboard:session')

class Registration(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('Dashboard:session')
    def __str__(self):
        return self.course.cnam

class Result(models.Model):
    reg = models.ForeignKey(Registration, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    ct1 = models.FloatField(null=True, blank=True)
    ct2 = models.FloatField(null=True, blank=True)
    ct3 = models.FloatField(null=True, blank=True)
    asn = models.FloatField(null=True, blank=True)
    # avg
    atd = models.IntegerField(null=True, blank=True)
    #total
    def __str__(self):
        return str(self.reg.session) + ' - ' + 'IT-' + str(self.reg.course.cidn) + ' - ' + self.student.snam
