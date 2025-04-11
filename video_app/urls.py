from django.urls import path
from .views import ListVideos, VideoDetail, ListInProgressVideos


urlpatterns = [
    path("videos/", ListVideos.as_view(), name="list-videos"),
    path("videos/in-progress/", ListInProgressVideos.as_view(), name="videos-in-progress"),
    path("video/<int:id>/", VideoDetail.as_view(), name="video-detail"),
]