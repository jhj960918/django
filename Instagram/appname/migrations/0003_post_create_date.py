# Generated by Django 3.0.8 on 2020-08-11 19:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appname', '0002_auto_20200811_2017'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 8, 12, 4, 19, 30, 769369), verbose_name='date published'),
        ),
    ]
