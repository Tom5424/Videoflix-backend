# Generated by Django 5.1.5 on 2025-04-09 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video_app', '0006_alter_video_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='video_progress',
            field=models.FloatField(default=0.0),
        ),
    ]
