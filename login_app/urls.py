from django.urls import path
from .views import GuestLoginView


urlpatterns = [
    path('guest-login/', GuestLoginView.as_view(), name='guest-login'),
]