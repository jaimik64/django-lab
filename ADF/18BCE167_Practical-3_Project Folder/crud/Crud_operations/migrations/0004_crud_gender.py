# Generated by Django 3.2.5 on 2021-09-07 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Crud_operations', '0003_auto_20210907_1241'),
    ]

    operations = [
        migrations.AddField(
            model_name='crud',
            name='Gender',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female')], default='male', max_length=10),
        ),
    ]
