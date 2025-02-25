from django.db import models


class Video(models.Model):
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=150)
    genres = models.CharField(max_length=20)
    created_on = models.DateField(auto_now_add=True)
    video_file = models.FileField(upload_to="videos")


    def __str__(self):
        return self.title