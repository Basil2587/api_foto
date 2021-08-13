from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly, IsAuthenticated
from .serializers import UserSerializer, AlbumSerializer, AlbumImageSerializer
from .models import Album, AlbumImage
from django.shortcuts import get_object_or_404
from .permissions import IsOwnerOrReadOnly


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
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
   # filter_backends = [DjangoFilterBackend]
   # filterset_fields = ["genres"]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class AlbumImageViewSet(viewsets.ModelViewSet):
    queryset = AlbumImage.objects.all()
    serializer_class = AlbumImageSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        queryset = AlbumImage.objects.filter(album=self.get_post()).all()
        return queryset

    def get_post(self):
        album = get_object_or_404(Album, id=self.kwargs["album_id"])
        return album

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, album=self.get_post())

'''
class AlbumImageViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    queryset = AlbumImage.objects.all()
    serializer_class = AlbumImageSerializer

'''