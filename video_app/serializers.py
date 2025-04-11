from .models import Video, Genre
from rest_framework import serializers


class GenreSerializer(serializers.ModelSerializer):


    class Meta:
        model = Genre
        fields = "__all__"


class VideoSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True, write_only=True)


    class Meta:
        model = Video
        fields = "__all__"
        

    def create(self, validated_data):
        genre_names = validated_data.pop("genre")
        video = Video.objects.create(**validated_data)
        for genre_name in genre_names:
            genre, created = Genre.objects.get_or_create(genre_name=genre_name)
        return video


class GenreWithVideosSerializer(serializers.ModelSerializer):
    videos = VideoSerializer(many=True)


    class Meta:
        model = Genre
        fields = ["genre_name", "videos"]



class DetailVideoSerializer(serializers.ModelSerializer):


    class Meta:
        model = Video
        fields = ["id", "title", "description", "created_on", "video_file", "video_image", "video_progress", "video_duration"]


    def validate_video_progress(self, value):
        if value < 0:
            raise serializers.ValidationError(["Progress cannot be a negative number!"])
        return round(value, 1)
    

    def validate_video_duration(self, value):
        if value < 0:
            raise serializers.ValidationError(["Duration cannot be a negative number!"])
        return round(value, 1)
