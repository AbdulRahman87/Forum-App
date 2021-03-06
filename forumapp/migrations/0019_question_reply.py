# Generated by Django 4.0.4 on 2022-04-20 10:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('forumapp', '0018_remove_question_ques_user_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='question_reply',
            fields=[
                ('reply_id', models.AutoField(primary_key=True, serialize=False)),
                ('reply_desc', models.TextField(default='')),
                ('reply_parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='forumapp.question')),
                ('reply_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
