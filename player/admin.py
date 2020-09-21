from django.contrib import admin
from .models import Player, Appointment


# Register your models here.
class PlayerAdmin(admin.ModelAdmin):
    list_display = ["full_name", "member_since", "playing_role", "batting_style", "bowling_style"]
    search_fields = ["full_name"]


class AppointmentAdmin(admin.ModelAdmin):
    list_display = ["name", "appointment_type", "season"]
    search_fields = ["name__full_name", "season"]
    list_filter = ["appointment_type"]


admin.site.register(Player, PlayerAdmin)
admin.site.register(Appointment, AppointmentAdmin)
