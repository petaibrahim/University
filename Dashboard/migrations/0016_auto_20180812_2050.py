# Generated by Django 2.1 on 2018-08-12 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0015_auto_20180812_0721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='avater'),
        ),
    ]
