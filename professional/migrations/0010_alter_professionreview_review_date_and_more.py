# Generated by Django 4.0.2 on 2022-10-17 10:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('professional', '0009_alter_professionreview_review_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professionreview',
            name='Review_Date',
            field=models.DateField(default=datetime.date(2022, 10, 17)),
        ),
        migrations.AlterField(
            model_name='professionreview',
            name='Review_Time',
            field=models.TimeField(default=datetime.datetime(2022, 10, 17, 15, 33, 10, 568207)),
        ),
        migrations.AlterField(
            model_name='professionreview_reply',
            name='Review_Reply_Date',
            field=models.DateField(default=datetime.date(2022, 10, 17)),
        ),
        migrations.AlterField(
            model_name='professionreview_reply',
            name='Review_Reply_Time',
            field=models.TimeField(default=datetime.datetime(2022, 10, 17, 15, 33, 10, 570211)),
        ),
    ]