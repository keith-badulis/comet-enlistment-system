# Generated by Django 2.2 on 2019-12-03 14:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('short', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=50)),
                ('subject_area', models.CharField(max_length=2)),
                ('catalog_num', models.CharField(max_length=5)),
                ('course_id', models.IntegerField()),
                ('units', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('short', models.CharField(max_length=10)),
                ('college', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.College')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.IntegerField(choices=[(0, 'unactivated'), (1, 'admin'), (2, 'student')], default=0)),
                ('slug', models.SlugField(default='hello-world')),
                ('id_number', models.IntegerField(default=0, unique=True)),
                ('college', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.College')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section_code', models.CharField(max_length=5)),
                ('max_cap', models.IntegerField(default=0)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('day', models.IntegerField(choices=[(1, 'Monday'), (2, 'Tuesday'), (3, 'Wednesday'), (4, 'Thursday'), (5, 'Friday'), (6, 'Monday and Wednesday'), (7, 'Tuesday and Thursday')])),
                ('course', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.Course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]