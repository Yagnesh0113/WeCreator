# Generated by Django 4.0.4 on 2022-09-16 11:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community_profession', '0009_alter_news_time_alter_news_comment_reply_reply_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='Date',
            field=models.DateField(default=datetime.date(2022, 9, 16)),
        ),
        migrations.AlterField(
            model_name='news',
            name='Time',
            field=models.TimeField(default=datetime.datetime(2022, 9, 16, 17, 0, 49, 738661)),
        ),
        migrations.AlterField(
            model_name='news_comment_reply',
            name='Reply_Time',
            field=models.TimeField(default=datetime.datetime(2022, 9, 16, 17, 0, 49, 738661)),
        ),
    ]
