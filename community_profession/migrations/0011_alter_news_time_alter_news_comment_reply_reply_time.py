# Generated by Django 4.0.2 on 2022-10-17 10:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community_profession', '0010_alter_news_date_alter_news_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='Time',
            field=models.TimeField(default=datetime.datetime(2022, 10, 17, 15, 59, 8, 595893)),
        ),
        migrations.AlterField(
            model_name='news_comment_reply',
            name='Reply_Time',
            field=models.TimeField(default=datetime.datetime(2022, 10, 17, 15, 59, 8, 613883)),
        ),
    ]