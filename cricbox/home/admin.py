from django.contrib import admin
from home.models import NewsItem, Podcast, Picture

# Register your models here.
class NewsAdmin(admin.ModelAdmin):
    model = NewsItem


class PodcastAdmin(admin.ModelAdmin):
    model = Podcast


class PicturesAdmin(admin.ModelAdmin):
    model = Picture


admin.site.register(NewsItem, NewsAdmin)
admin.site.register(Podcast, PodcastAdmin)
admin.site.register(Picture, PicturesAdmin)
