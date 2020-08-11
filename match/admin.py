from django.contrib import admin

from .models import Match
from bowler.models import Bowler

# Register your models here.
class BowlerInline(admin.TabularInline):
    model = Bowler
    extra = 1


class MatchAdmin(admin.ModelAdmin):
    inlines = [BowlerInline]
    list_display = ("opposition", "played", "result", "venue", "mtype")
    list_filter = ["played", "home_or_away", "mtype"]
    search_fields = ["opposition__name", "venue__name"]


admin.site.register(Match, MatchAdmin)
