from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import UserViewSet, AlbumViewSet, AlbumImageViewSet


users_router = DefaultRouter()
users_router.register('', UserViewSet)
users_router.register("album", AlbumViewSet, basename="album")
users_router.register(
    r"album/(?P<album_id>\d+)/foto", AlbumImageViewSet, basename="foto")


urlpatterns = [
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path('users/', include(users_router.urls)),
]
