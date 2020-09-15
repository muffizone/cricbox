from django.db import models
from .choices import PLAYING_ROLES, BATTING_STYLES, BOWLING_STYLES


class Player(models.Model):
    full_name = models.CharField(max_length=50, primary_key=True)
    member_since = models.DateField("Date Joined", null=True, blank=True)
    email = models.EmailField("Email", null=True, blank=True)
    playing_role = models.TextField(choices=PLAYING_ROLES, blank=True)
    batting_style = models.TextField(choices=BATTING_STYLES, blank=True)
    bowling_style = models.TextField(choices=BOWLING_STYLES, blank=True)

    class Meta:
        ordering = ["full_name"]
        db_table = "players"

    def __str__(self):
        return self.full_name

