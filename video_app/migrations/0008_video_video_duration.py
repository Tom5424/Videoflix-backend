# Generated by Django 5.1.5 on 2025-04-11 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video_app', '0007_video_video_progress'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='video_duration',
            field=models.FloatField(default=0.0),
        ),
    ]
