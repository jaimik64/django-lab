# Generated by Django 4.1 on 2022-11-15 12:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='image',
            field=models.ImageField(default=django.utils.timezone.now, max_length=200, upload_to='uploads/'),
            preserve_default=False,
        ),
    ]
