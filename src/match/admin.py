from django.contrib import admin
from .models import Match
from match.models import PlayerMatchAttribute


# Register your models here.
class PlayerInline(admin.TabularInline):
    model = PlayerMatchAttribute


class MatchAdmin(admin.ModelAdmin):
    list_display = ("opposition", "date", "venue", "mtype")
    list_filter = ["date", "home_or_away", "mtype"]
    search_fields = ["opposition__name", "venue__name", "mtype"]
    filter_horizontal = ("players", )
    inlines = (PlayerInline, )
    date_hierarchy = "date"



admin.site.register(Match, MatchAdmin)
