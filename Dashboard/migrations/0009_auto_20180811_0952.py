# Generated by Django 2.1 on 2018-08-11 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0008_auto_20180810_1858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='sesid',
            field=models.IntegerField(primary_key=True, serialize=False, verbose_name='Session'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='ulogo',
            field=models.ImageField(blank=True, upload_to='media'),
        ),
    ]
