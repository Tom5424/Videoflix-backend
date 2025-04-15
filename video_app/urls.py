from django.urls import path
from .views import ListUnwatchedVideos, ListWatchedVideos, VideoDetail


urlpatterns = [
    path("unwatched-videos/", ListUnwatchedVideos.as_view(), name="list-unwatched-videos"),
    path("watched-videos/", ListWatchedVideos.as_view(), name="list-watched-videos"),
    path("video/<int:id>/", VideoDetail.as_view(), name="video-detail"),
]