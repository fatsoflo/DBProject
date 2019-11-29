# Generated by Django 2.2.7 on 2019-11-29 04:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('user', models.OneToOneField(default='student', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='user.AppUser')),
                ('major', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='school.Major')),
                ('school', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='school.School')),
            ],
        ),
    ]
