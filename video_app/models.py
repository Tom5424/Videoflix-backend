from .tasks import convert_to_360p
from django.db import models
import os


class Genre(models.Model):
    genre_name = models.CharField(max_length=20, unique=True) 


    def __str__(self):
        return self.genre_name   


class Video(models.Model):
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=150)
    genres = models.ManyToManyField(Genre, related_name="videos")
    created_on = models.DateField(auto_now_add=True)
    video_file = models.FileField(upload_to="videos")


    def save(self):
        super().save()
        convert_to_360p(self.video_file.path)
        print("Video uploaded.")


    def delete(self):
        if os.path.isfile(self.video_file.path):
            os.remove(self.video_file.path)
            print("Video deleted.")
        return super().delete()
    

    def __str__(self):
        return self.title