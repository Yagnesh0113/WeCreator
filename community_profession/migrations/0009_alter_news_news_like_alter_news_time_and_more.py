# Generated by Django 4.0.2 on 2022-09-26 12:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0001_initial'),
        ('community_profession', '0008_alter_bookmark_post_alter_news_date_alter_news_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='News_like',
            field=models.ManyToManyField(blank=True, null=True, related_name='News_like', to='Account.UserProfile'),
        ),
        migrations.AlterField(
            model_name='news',
            name='Time',
            field=models.TimeField(default=datetime.datetime(2022, 9, 26, 17, 47, 2, 487673)),
        ),
        migrations.AlterField(
            model_name='news_comment',
            name='News_comment_like',
            field=models.ManyToManyField(blank=True, null=True, related_name='News_comment_like', to='Account.UserProfile'),
        ),
        migrations.AlterField(
            model_name='news_comment_reply',
            name='Reply_Time',
            field=models.TimeField(default=datetime.datetime(2022, 9, 26, 17, 47, 2, 491671)),
        ),
        migrations.AlterField(
            model_name='post_commment',
            name='Comment_like',
            field=models.ManyToManyField(blank=True, null=True, related_name='Comment_like', to='Account.UserProfile'),
        ),
        migrations.AlterField(
            model_name='user_answer',
            name='Answer_Like',
            field=models.ManyToManyField(blank=True, null=True, related_name='Answer_Like', to='Account.UserProfile'),
        ),
        migrations.AlterField(
            model_name='user_question',
            name='Question_Like',
            field=models.ManyToManyField(blank=True, null=True, related_name='Question_Like', to='Account.UserProfile'),
        ),
        migrations.AlterField(
            model_name='userpost',
            name='Like',
            field=models.ManyToManyField(blank=True, null=True, related_name='liked', to='Account.UserProfile'),
        ),
    ]
