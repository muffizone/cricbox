from django.contrib import admin
from .models import MatchStatistics
from batsman.models import Batsman
from bowler.models import Bowler


# Register your models here.
class BatsmanInline(admin.TabularInline):
    model = Batsman
    extra = 1


class BowlerInline(admin.TabularInline):
    model = Bowler
    extra = 1


class MatchStatisticsAdmin(admin.ModelAdmin):
    inlines = (BatsmanInline, BowlerInline)


admin.site.register(MatchStatistics, MatchStatisticsAdmin)