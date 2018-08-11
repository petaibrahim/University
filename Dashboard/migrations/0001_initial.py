# Generated by Django 2.1 on 2018-08-09 09:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('cid', models.AutoField(primary_key=True, serialize=False)),
                ('cnam', models.CharField(max_length=200)),
                ('cidn', models.IntegerField()),
                ('cred', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Enrol',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ct1', models.FloatField(blank=True, null=True)),
                ('ct2', models.FloatField(blank=True, null=True)),
                ('ct3', models.FloatField(blank=True, null=True)),
                ('asn', models.FloatField(blank=True, null=True)),
                ('atd', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Reg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Dashboard.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('sesid', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('snam', models.CharField(max_length=200)),
                ('sid', models.AutoField(primary_key=True, serialize=False)),
                ('sroll', models.IntegerField()),
                ('sreg', models.IntegerField()),
                ('sbtc', models.IntegerField()),
                ('sses', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('unam', models.CharField(max_length=200)),
                ('uid', models.AutoField(primary_key=True, serialize=False)),
                ('umob', models.IntegerField()),
                ('umail', models.EmailField(max_length=254)),
                ('uimg', models.CharField(default='null', max_length=1000)),
            ],
        ),
        migrations.AddField(
            model_name='reg',
            name='session',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Dashboard.Session'),
        ),
        migrations.AddField(
            model_name='reg',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Dashboard.User'),
        ),
        migrations.AddField(
            model_name='enrol',
            name='reg',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Dashboard.Reg'),
        ),
        migrations.AddField(
            model_name='enrol',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Dashboard.Student'),
        ),
    ]