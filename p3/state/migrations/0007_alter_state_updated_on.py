# Generated by Django 4.1 on 2022-11-01 11:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('state', '0006_alter_state_updated_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='state',
            name='updated_on',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='updatedon'),
        ),
    ]