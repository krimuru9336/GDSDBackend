# Generated by Django 3.2.9 on 2022-01-22 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AllUsers', '0003_auto_20220122_1829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activeclasses',
            name='class_review',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='activeclasses',
            name='feedback_in_words',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='activeclasses',
            name='rating_by_student',
            field=models.IntegerField(blank=True),
        ),
    ]
