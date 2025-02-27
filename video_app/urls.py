from django.urls import path
from .views import ListVideos, SingleVideo


urlpatterns = [
    path("videos/", ListVideos.as_view(), name="list-videos"),
    path("video/<int:id>/", SingleVideo.as_view(), name="single-video"),
]