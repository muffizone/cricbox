from django.contrib import admin
from .models import Batsman, WicketType


# Register your models here.
class WicketTypeAdmin(admin.ModelAdmin):
    pass


class BatsmanAdmin(admin.ModelAdmin):
    list_display = ("player", "how_out", "bowler", "runs", "match_statistics")
    list_filter = ["how_out"]
    search_fields = ["player__full_name", "bowler"]


admin.site.register(Batsman, BatsmanAdmin)
admin.site.register(WicketType, WicketTypeAdmin)

