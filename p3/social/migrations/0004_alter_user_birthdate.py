# Generated by Django 4.1 on 2022-11-15 11:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0003_alter_user_birthdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birthdate',
            field=models.DateField(default=datetime.date(2022, 11, 15), verbose_name='Date'),
        ),
    ]