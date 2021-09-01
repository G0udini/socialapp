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

from .views import dashboard, register, edit, user_follow, user_list, user_detail

# app_name = "account"
urlpatterns = [
    path("edit/", edit, name="edit"),
    path("register/", register, name="register"),
    path("", include("django.contrib.auth.urls")),
    path("dashboard/", dashboard, name="dashboard"),
    path("users/", user_list, name="user_list"),
    path("users/follow/", user_follow, name="user_follow"),
    path("users/<username>/", user_detail, name="user_detail"),
]
