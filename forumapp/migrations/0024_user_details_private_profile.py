# Generated by Django 3.2.8 on 2022-06-30 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forumapp', '0023_rename_contact_contactus'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_details',
            name='private_profile',
            field=models.CharField(default='off', max_length=5),
            preserve_default=False,
        ),
    ]
