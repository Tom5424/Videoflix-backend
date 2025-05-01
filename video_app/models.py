from video_app.tasks import create_video_image, converts_to_multi_qualities_and_hls_format
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
    video_duration = models.FloatField(default=0.0)


    def save(self, *args, **kwargs):
        video_was_new_uploaded = self._state.adding  # Checks if instanz already exist
        super().save(*args, **kwargs)
        if not self.image_created: 
            self.image_created = True
            create_video_image(self)
        if video_was_new_uploaded:     
            converts_to_multi_qualities_and_hls_format.delay(self.video_file.path)
            print("Video uploaded.")


    def get_hls_master_playlist_url(self):
        file_name = os.path.splitext(os.path.basename(self.video_file.name))[0]
        return f"/media/hls-outputs/{file_name}_master.m3u8"     


    def delete(self):
        if os.path.isfile(self.video_file.path):
            os.remove(self.video_file.path)
            print("Video deleted.")
        return super().delete()
    

    def __str__(self):
        return self.title