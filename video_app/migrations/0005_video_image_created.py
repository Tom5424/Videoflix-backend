# Generated by Django 5.1.5 on 2025-03-30 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video_app', '0004_alter_video_video_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='image_created',
            field=models.BooleanField(default=False),
        ),
    ]
