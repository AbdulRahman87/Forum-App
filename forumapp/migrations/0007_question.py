# Generated by Django 3.2.8 on 2022-04-16 11:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forumapp', '0006_alter_categories_cat_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ques_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forumapp.categories')),
            ],
        ),
    ]
