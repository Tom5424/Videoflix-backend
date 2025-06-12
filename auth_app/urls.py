from django.urls import path, include
from dj_rest_auth.views import PasswordResetConfirmView
from registration_app.views import CustomVerifyEmailView


urlpatterns = [
    path("registration/", include("dj_rest_auth.registration.urls")),
    path("registration/verify-email/", CustomVerifyEmailView.as_view(), name="custom-verify-email"),
    path("password/reset/confirm/<uidb64>/<token>/", PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path("guest-login/", include("login_app.urls")),
    path("", include("dj_rest_auth.urls")),
]