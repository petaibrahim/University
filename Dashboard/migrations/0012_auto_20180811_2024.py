# Generated by Django 2.1 on 2018-08-11 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0011_auto_20180811_1949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='ulogo',
            field=models.ImageField(blank=True, upload_to='avater'),
        ),
    ]
