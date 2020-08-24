from django.contrib import admin
from .models import Player


# Register your models here.
class PlayerAdmin(admin.ModelAdmin):
    list_display = ["full_name", "member_since"]
    search_fields = ["full_name"]


admin.site.register(Player, PlayerAdmin)
