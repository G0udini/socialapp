from django.urls import path, include
# from django.contrib.auth.views import (
#     LoginView,
#     LogoutView,
#     PasswordChangeDoneView,
#     PasswordChangeView,
#     PasswordResetDoneView,
#     PasswordResetView,
#     PasswordResetConfirmView,
#     PasswordResetCompleteView,
# )

from .views import dashboard

# app_name = "account"
urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    path("dashboard/", dashboard, name="dashboard"),
]
