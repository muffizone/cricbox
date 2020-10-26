from django.contrib import admin
from .models import Match, MatchType, HomeAway, PlayerSkill
from match.models import PlayerMatchAttribute


# Register your models here.
class MatchTypeAdmin(admin.ModelAdmin):
    pass


class HomeAwayAdmin(admin.ModelAdmin):
    pass


class PlayerSkillAdmin(admin.ModelAdmin):
    pass


class PlayerInlineAdmin(admin.TabularInline):
    model = PlayerMatchAttribute


class MatchAdmin(admin.ModelAdmin):
    list_display = ("opposition", "date", "venue", "mtype")
    list_filter = ["date", "home_or_away", "mtype"]
    search_fields = ["opposition__name", "venue__name", "mtype"]
    filter_horizontal = ("players",)
    inlines = (PlayerInlineAdmin,)
    date_hierarchy = "date"


admin.site.register(Match, MatchAdmin)
admin.site.register(MatchType, MatchTypeAdmin)
admin.site.register(PlayerSkill, PlayerSkillAdmin)
admin.site.register(HomeAway, HomeAwayAdmin)
