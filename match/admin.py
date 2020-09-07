from django.contrib import admin
from .models import Match
from match.models import PlayerMatchAttribute


# Register your models here.
class PlayerInline(admin.TabularInline):
    model = PlayerMatchAttribute


class MatchAdmin(admin.ModelAdmin):
    list_display = ("opposition", "date", "venue", "mtype")
    list_filter = ["date", "home_or_away", "mtype"]
    search_fields = ["opposition__name", "venue__name"]
    filter_horizontal = ("players", )
    inlines = (PlayerInline, )


admin.site.register(Match, MatchAdmin)
