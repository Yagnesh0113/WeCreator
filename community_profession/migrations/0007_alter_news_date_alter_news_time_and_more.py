# Generated by Django 4.0.4 on 2022-09-22 05:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community_profession', '0006_alter_news_date_alter_news_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='Date',
            field=models.DateField(default=datetime.date(2022, 9, 22)),
        ),
        migrations.AlterField(
            model_name='news',
            name='Time',
            field=models.TimeField(default=datetime.datetime(2022, 9, 22, 10, 55, 9, 934166)),
        ),
        migrations.AlterField(
            model_name='news_comment_reply',
            name='Reply_Time',
            field=models.TimeField(default=datetime.datetime(2022, 9, 22, 10, 55, 9, 934166)),
        ),
    ]