# Generated by Django 3.1.8 on 2021-08-19 20:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='registration_date',
        ),
    ]
