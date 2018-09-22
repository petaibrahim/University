from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import RegexValidator
from smart_selects.db_fields import ChainedForeignKey
from PIL import Image


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
    phone_regex = RegexValidator(regex=r'^\0?1?\d{11}$')
    mobile = models.CharField(validators=[phone_regex], max_length=11, blank=True)
    avatar = models.ImageField(upload_to='avatar', blank=True, null=True)

    def __str__(self):
        return self.user.first_name + ' '+self.user.last_name

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Teacher.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.teacher.save()

class Session(models.Model):
    sesid = models.IntegerField(primary_key=True,verbose_name= ('Session'))

    def __str__(self):
        return str(self.sesid)
    def get_absolute_url(self):
        return reverse('Dashboard:session')

class Registration(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("Dashboard:session")

    def __str__(self):
        return str(self.session) + " - " + self.course.cnam + " - "

class Assignation(models.Model):
    reg = models.ForeignKey(Registration, on_delete=models.CASCADE, null=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.reg.session.sesid)  + " - IT-" + str(self.reg.course.cidn) +  " - " + str(self.reg.course.cnam) +  " - " + self.teacher.user.first_name + ' '+self.teacher.user.last_name

class Result(models.Model):
    asign = models.ForeignKey(Assignation, on_delete=models.CASCADE, null=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
    ct1 = models.FloatField(null=True, blank=True)
    ct2 = models.FloatField(null=True, blank=True)
    ct3 = models.FloatField(null=True, blank=True)
    ct4 = models.FloatField(null=True, blank=True)
    asn = models.FloatField(null=True, blank=True)
    avg = models.FloatField(null=True, blank=True)
    atd = models.IntegerField(null=True, blank=True)
    total = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.asign.reg.session) + ' - ' + 'IT-' + str(self.asign.reg.course.cidn) + ' - ' + self.student.snam