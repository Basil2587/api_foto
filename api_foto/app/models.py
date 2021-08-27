from django.db import models
from django.contrib.auth import get_user_model
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit


User = get_user_model()


class Tag(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Album(models.Model):
    title = models.CharField(max_length=70)
    author = models.ForeignKey(User, null=True,
                               blank=True, on_delete=models.CASCADE,
                               related_name="album")
    date_created = models.DateTimeField("Дата создания", auto_now_add=True)
    date_modified = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class AlbumImage(models.Model):
    image_id = models.AutoField(primary_key=True)
    album = models.ForeignKey(Album,
                              db_column='album_id',  null=True,
                              on_delete=models.CASCADE,
                              verbose_name="фотоальбом")
    title = models.CharField(max_length=255)
    original_image = models.ImageField(
        upload_to="album/", blank=True, null=True, verbose_name="Картинка")
    small_image = ImageSpecField(
        source='original_image', processors=[ResizeToFit(150)],
        format='JPEG', options={'quality': 80})
    tag = models.ManyToManyField(Tag, verbose_name="Тэг")
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
