from django.contrib import admin
from .models import (
    Player,
    Appointment,
    PlayingRole,
    BattingStyle,
    BowlingStyle,
    AppointmentType,
)


# Register your models here.
class PlayingRoleAdmin(admin.ModelAdmin):
    pass


class BattingStyleAdmin(admin.ModelAdmin):
    pass


class BowlingStyleAdmin(admin.ModelAdmin):
    pass


class AppointmentTypeAdmin(admin.ModelAdmin):
    pass


class PlayerAdmin(admin.ModelAdmin):
    list_display = [
        "first_name",
        "last_name",
        "member_since",
        "playing_role",
        "batting_style",
        "bowling_style",
    ]
    search_fields = ["first_name", "last_name"]
    list_filter = ["playing_role", "batting_style", "bowling_style"]


class AppointmentAdmin(admin.ModelAdmin):
    list_display = ["name", "appointment_type", "season"]
    search_fields = ["name__full_name", "season"]
    list_filter = ["appointment_type"]


admin.site.register(Player, PlayerAdmin)
admin.site.register(Appointment, AppointmentAdmin)
admin.site.register(PlayingRole, PlayingRoleAdmin)
admin.site.register(BattingStyle, BattingStyleAdmin)
admin.site.register(BowlingStyle, BowlingStyleAdmin)
admin.site.register(AppointmentType, AppointmentTypeAdmin)
