# Generated by Django 2.2 on 2019-12-04 10:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20191204_1800'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='class',
            name='students',
        ),
        migrations.AddField(
            model_name='profile',
            name='classes',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Class'),
        ),
    ]