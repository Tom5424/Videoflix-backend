from django.urls import path
from .views import ListVideos


urlpatterns = [
    path("videos/", ListVideos.as_view(), name="list-videos"),
]