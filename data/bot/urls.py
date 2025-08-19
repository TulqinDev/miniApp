from django.urls import path, include

from data.bot.views import *

urlpatterns = [
    path("access/", JWTtokenGenerator.as_view(), name="access"),
    path("refresh/", JWTtokenRefresh.as_view(), name="refresh"),
    path("me/", Me.as_view(), name="me"),
]
