# Generated by Django 4.0.4 on 2022-04-17 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forumapp', '0010_alter_user_details__user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_details',
            name='user_img',
            field=models.ImageField(default='/static/IMG/user.png', upload_to='user_img/images'),
        ),
    ]