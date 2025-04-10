from video_app.tasks import convert_to_360p, create_video_image
from django.db import models
import os


class Genre(models.Model):
    genre_name = models.CharField(max_length=20, unique=True) 


    def __str__(self):
        return self.genre_name   


class Video(models.Model):
    title = models.CharField(max_length=15)
    description = models.CharField(max_length=150)
    genres = models.ManyToManyField(Genre, related_name="videos")
    created_on = models.DateField(auto_now_add=True)
    video_file = models.FileField(upload_to="videos")
    video_image = models.ImageField(upload_to="video-images", null=True)
    image_created = models.BooleanField(default=False)
    video_progress = models.FloatField(default=0.0)


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.image_created: 
            self.image_created = True
            create_video_image(self)
        convert_to_360p.delay(self.video_file.path)
        print("Video uploaded.")


    def delete(self):
        if os.path.isfile(self.video_file.path):
            os.remove(self.video_file.path)
            print("Video deleted.")
        return super().delete()
    

    def __str__(self):
        return self.title