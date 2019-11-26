# Generated by Django 2.2.7 on 2019-11-26 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Major',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('major_name', models.CharField(choices=[('AR', 'Art'), ('BI', 'Business'), ('CE', 'Civil Engineering'), ('CS', 'Computer Science'), ('FI', 'Film'), ('FN', 'Finance'), ('HI', 'History'), ('MT', 'Math'), ('MU', 'Music')], max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_name', models.CharField(max_length=30)),
                ('school_address', models.CharField(max_length=200)),
            ],
        ),
    ]
