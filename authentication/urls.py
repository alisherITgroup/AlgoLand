from django.urls import path
from .views import login, signup, profile, users

urlpatterns = [
    path("login/", login, name="login"),
    path("signup/", signup, name="signup"),
    path("users/", users, name="users"),
    path("profile/<str:username>/", profile, name="profile")
]