# Generated by Django 3.2.9 on 2022-01-02 21:54

import AllUsers.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AllUsers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fuldemyuser',
            name='profile_pic',
            field=models.ImageField(default='posts/default.jpg', upload_to=AllUsers.models.user_directory_path),
        ),
    ]