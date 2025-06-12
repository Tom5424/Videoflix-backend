from django.urls import path
from .views import GuestLoginView


urlpatterns = [
    path("", GuestLoginView.as_view(), name='guest-login'),
]