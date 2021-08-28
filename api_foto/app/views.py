from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import UserSerializer, AlbumSerializer, AlbumImageSerializer
from .models import Album, AlbumImage
from django.shortcuts import get_object_or_404
from .permissions import IsOwnerOrReadOnly


User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            self.permission_classes = (AllowAny,)

        return super(UserViewSet, self).get_permissions()


class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        users = get_object_or_404(User, id=self.kwargs['users_pk'])
        queryset = Album.objects.filter(author=users)
        return queryset

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class AlbumImageViewSet(viewsets.ModelViewSet):
    serializer_class = AlbumImageSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        album = get_object_or_404(Album, id=self.kwargs['album_pk'])
        queryset = AlbumImage.objects.filter(album=album)
        return queryset

    def perform_create(self, serializer):
        album = get_object_or_404(Album, id=self.kwargs['album_pk'])
        serializer.save(album=album)
