from django.db import models
from .choices import PLAYING_ROLES, BATTING_STYLES, BOWLING_STYLES, APPOINTMENT_TYPES
import datetime


class Player(models.Model):
    full_name = models.CharField(max_length=50)
    member_since = models.DateField("Date Joined", null=True, blank=True)
    email = models.EmailField("Email", null=True, blank=True)
    playing_role = models.TextField(choices=PLAYING_ROLES, blank=True)
    batting_style = models.TextField(choices=BATTING_STYLES, blank=True)
    bowling_style = models.TextField(choices=BOWLING_STYLES, blank=True)
    active = models.BooleanField(blank=True, default=True)

    class Meta:
        ordering = ["full_name"]
        db_table = "players"

    def __str__(self):
        return self.full_name


class Appointment(models.Model):
    YEARS = []
    for year in range(1997, datetime.datetime.now().year + 1):
        YEARS.append((year, year))

    name = models.ForeignKey(Player, on_delete=models.DO_NOTHING)
    appointment_type = models.TextField("Appointment Type", choices=APPOINTMENT_TYPES)
    season = models.IntegerField(
        "Season", default=datetime.datetime.now().year, choices=YEARS
        )

    class Meta:
        ordering = ["-season"]
        db_table = "appointments"

    def __str__(self):
        return f"{self.name}-{self.appointment_type}"
