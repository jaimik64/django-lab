# Generated by Django 3.2.5 on 2022-10-14 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postfile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postfile1',
            name='cover',
            field=models.FileField(upload_to='files/'),
        ),
    ]