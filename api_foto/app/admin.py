from django.contrib import admin

from .models import Album, AlbumImage, Tag


class TagsAdmin(admin.ModelAdmin):
    list_display = ("id", "name",)
    search_fields = ("name",)
    list_filter = ("name",)
    empty_value_display = "-пусто-"


class AlbumAdmin(admin.ModelAdmin):
    list_display = ("pk", "title", "author", "date_created")
    search_fields = ("author",)
    list_filter = ("title",)
    empty_value_display = "-пусто-"


class AlbumImageAdmin(admin.ModelAdmin):
    list_display = ("image_id", "album", "title",
                    "original_image", "small_image", "date_created")
    search_fields = ("album",)
    list_filter = ("album", "tag", "date_created")
    empty_value_display = "-пусто-"


admin.site.register(Tag, TagsAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(AlbumImage, AlbumImageAdmin)
