from django.contrib import admin
from .models import Batsman


# Register your models here.
class BatsmanAdmin(admin.ModelAdmin):
    list_display = ("player", "how_out", "bowler", "runs", "match")
    list_filter = ["how_out"]
    search_fields = ["player__full_name", "bowler"]


admin.site.register(Batsman, BatsmanAdmin)
