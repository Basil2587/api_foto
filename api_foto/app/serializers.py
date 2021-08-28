from rest_framework import serializers
from .models import Album, AlbumImage
from django.contrib.auth import get_user_model


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = (
            'id',
            'username',
            'password',
            'email',
        )
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        user = get_user_model().objects.create_user(**validated_data)
        return user

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)
        return super(UserSerializer, self).update(instance, validated_data)


class AlbumSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.username")
    foto_count = serializers.SerializerMethodField()

    def get_foto_count(self, obj):
        foto_count = AlbumImage.objects.filter(album__in=[obj]).count()
        return foto_count

    class Meta:
        fields = ("id", "title", "author", "foto_count", "date_created")
        model = Album


class AlbumImageSerializer(serializers.ModelSerializer):
    small_image = serializers.ImageField()
    tag = serializers.SlugRelatedField(
            many=True, slug_field='name', read_only=True)

    class Meta:
        fields = '__all__'
        model = AlbumImage
