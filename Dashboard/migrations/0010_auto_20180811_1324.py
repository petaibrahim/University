# Generated by Django 2.1 on 2018-08-11 13:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0009_auto_20180811_0952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='teacher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Dashboard.Teacher'),
        ),
    ]
