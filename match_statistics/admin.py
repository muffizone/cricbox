from django.contrib import admin
from .models import MatchStatistics


# Register your models here
class MatchStatisticsAdmin(admin.ModelAdmin):
    list_display = ("opposition", "date", "venue", "mtype",  "result")
    list_filter = ["match__date", "match__mtype", "match__home_or_away", "result" ]
    date_hierarchy = "match__date"

    def date(self, x):
        return x.match.date

    def opposition(self, x):
        return x.match.opposition.name

    def venue(self, x):
        return x.match.venue.name

    def mtype(self, x):
        return x.match.get_mtype_display()

    mtype.short_description = "Type"


admin.site.register(MatchStatistics, MatchStatisticsAdmin)
