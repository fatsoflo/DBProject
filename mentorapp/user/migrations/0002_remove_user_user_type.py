# Generated by Django 2.2.7 on 2019-11-26 18:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='user_type',
        ),
    ]
