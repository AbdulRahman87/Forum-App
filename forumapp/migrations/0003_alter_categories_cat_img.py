# Generated by Django 4.0.4 on 2022-04-12 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forumapp', '0002_alter_categories_cat_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='cat_img',
            field=models.ImageField(blank=True, null=True, upload_to='forum_cat/images'),
        ),
    ]
