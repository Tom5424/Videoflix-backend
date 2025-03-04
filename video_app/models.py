from django.db import models


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


    def __str__(self):
        return self.title