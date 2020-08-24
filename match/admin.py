from django.contrib import admin

from .models import Match
from bowler.models import Bowler
from batsman.models import Batsman


# Register your models here.
class BowlerInline(admin.TabularInline):
    model = Bowler
    extra = 1


class BatsmanInline(admin.TabularInline):
    model = Batsman
    extra = 1


class MatchAdmin(admin.ModelAdmin):
    inlines = [BowlerInline, BatsmanInline]
    list_display = ("opposition", "played", "result", "venue", "mtype")
    list_filter = ["played", "home_or_away", "mtype"]
    search_fields = ["opposition__name", "venue__name"]


admin.site.register(Match, MatchAdmin)
