# Generated by Django 2.2 on 2019-12-04 15:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20191204_1858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='program',
            name='college',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.College'),
        ),
    ]
