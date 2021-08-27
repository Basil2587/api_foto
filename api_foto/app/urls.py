from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import UserViewSet, AlbumViewSet, AlbumImageViewSet
from rest_framework_nested import routers


router = DefaultRouter()
router.register('users', UserViewSet, 'users')
album_router = routers.NestedSimpleRouter(router, r"users", lookup="users")
album_router.register(r"album", AlbumViewSet, basename="album")
image_router = routers.NestedSimpleRouter(
                album_router, r"album", lookup="album")
image_router.register(r"foto", AlbumImageViewSet, basename="foto")


urlpatterns = [
    path("", include(router.urls)),
    path("", include(album_router.urls)),
    path("", include(image_router.urls)),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),

]
