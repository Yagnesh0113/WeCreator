# Generated by Django 4.0.4 on 2022-09-07 04:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('professional', '0007_merge_20220906_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professionreview',
            name='Review_Date',
            field=models.DateField(default=datetime.date(2022, 9, 7)),
        ),
        migrations.AlterField(
            model_name='professionreview',
            name='Review_Time',
            field=models.TimeField(default=datetime.datetime(2022, 9, 7, 10, 20, 20, 903253)),
        ),
        migrations.AlterField(
            model_name='professionreview_reply',
            name='Review_Reply_Date',
            field=models.DateField(default=datetime.date(2022, 9, 7)),
        ),
        migrations.AlterField(
            model_name='professionreview_reply',
            name='Review_Reply_Time',
            field=models.TimeField(default=datetime.datetime(2022, 9, 7, 10, 20, 20, 903253)),
        ),
    ]
