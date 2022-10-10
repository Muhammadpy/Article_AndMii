from django.urls import path
from .views import *


app_name = "follower"

urlpatterns = [
    path('register/', register, name='register'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path("login/", LoginView.as_view(), name="login"),
]