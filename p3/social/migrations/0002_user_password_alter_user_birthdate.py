# Generated by Django 4.1 on 2022-10-04 06:31

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default=django.utils.timezone.now, max_length=18),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='birthdate',
            field=models.DateField(default=datetime.date(2022, 10, 4), verbose_name='Date'),
        ),
    ]
