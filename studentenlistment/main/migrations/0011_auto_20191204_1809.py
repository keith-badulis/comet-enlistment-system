# Generated by Django 2.2 on 2019-12-04 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20191204_1805'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='classes',
        ),
        migrations.AddField(
            model_name='profile',
            name='classes',
            field=models.ManyToManyField(blank=True, to='main.Class'),
        ),
    ]
