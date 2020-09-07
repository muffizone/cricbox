from django.db import models

from django.db.models import Q

from venue.models import Venue
from opposition.models import Opposition
from player.models import Player
import datetime


# Create your models here.
class MatchType(models.TextChoices):
    FRIENDLY = "F"
    LEAGUE = "L"
    VPCCL = "V"
    OTHERS = "O"


class HomeAway(models.TextChoices):
    HOME = "H"
    AWAY = "A"


class Match(models.Model):
    YEARS = []
    for year in range(1997, datetime.datetime.now().year + 1):
        YEARS.append((year, year))

    season = models.IntegerField(
        "Season", default=datetime.datetime.now().year, choices=YEARS
        )
    date = models.DateField("Date")
    mtype = models.TextField("Type", choices=MatchType.choices)
    home_or_away = models.TextField("Home or Away", choices=HomeAway.choices)
    remarks = models.CharField(
        "Remarks", blank=True, max_length=200)
    opposition = models.ForeignKey(
        Opposition, on_delete=models.PROTECT, blank=True, null=True
        )
    venue = models.ForeignKey(Venue, on_delete=models.PROTECT, blank=True, null=True)
    players = models.ManyToManyField(Player, blank=True, through='PlayerMatchAttribute')

    class Meta:
        ordering = ["-date"]
        verbose_name_plural = "matches"
        db_table = "matches"

    def __str__(self):
        return f"London Fields vs {self.opposition} at {self.venue}, {self.date.strftime('%d %b, %Y')}"


class PlayerSkills(models.TextChoices):
    BOWLER = "BW"
    BATSMAN = "BT"
    ALL_ROUNDER = "AR"
    WICKET_KEEPER = "WK"


class PlayerMatchAttribute(models.Model):
    player = models.ForeignKey(Player, on_delete=models.SET_NULL, null=True)
    match = models.ForeignKey(Match, on_delete=models.SET_NULL, null=True)
    skill = models.TextField("Skill Set", blank=True, null=True, choices=PlayerSkills.choices)
    captain = models.BinaryField("Captain", default=False)

    class Meta:
        db_table = "player_match_attributes"