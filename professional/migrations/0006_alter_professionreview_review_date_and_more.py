# Generated by Django 4.0.4 on 2022-09-20 10:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('professional', '0005_alter_professionreview_review_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professionreview',
            name='Review_Date',
            field=models.DateField(default=datetime.date(2022, 9, 20)),
        ),
        migrations.AlterField(
            model_name='professionreview',
            name='Review_Time',
            field=models.TimeField(default=datetime.datetime(2022, 9, 20, 16, 17, 18, 766364)),
        ),
        migrations.AlterField(
            model_name='professionreview_reply',
            name='Review_Reply_Date',
            field=models.DateField(default=datetime.date(2022, 9, 20)),
        ),
        migrations.AlterField(
            model_name='professionreview_reply',
            name='Review_Reply_Time',
            field=models.TimeField(default=datetime.datetime(2022, 9, 20, 16, 17, 18, 768363)),
        ),
    ]
