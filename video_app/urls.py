from django.urls import path
from .views import ListVideos, VideoDetail


urlpatterns = [
    path("videos/", ListVideos.as_view(), name="list-videos"),
    path("video/<int:id>/", VideoDetail.as_view(), name="video-detail"),
]