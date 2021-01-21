from django.contrib import admin

from .models import Bowler


# Register your models here.
class BowlerAdmin(admin.ModelAdmin):
    list_display = ("player", "overs", "maidens", "runs", "wickets", "match_statistics")
    search_fields = ["player__full_name"]


admin.site.register(Bowler, BowlerAdmin)
