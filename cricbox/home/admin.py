# Cricbox imports
from home.models import NewsItem, Picture, Podcast

# Django imports
from django.contrib import admin


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
