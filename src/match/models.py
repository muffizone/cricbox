from django.db import models
from venue.models import Venue
from opposition.models import Opposition
from player.models import Player
import datetime
from .choices import MATCH_TYPE, HOME_AWAY, PLAYER_SKILLS


# Create your models here.
class Match(models.Model):
    YEARS = []
    for year in range(1997, datetime.datetime.now().year + 1):
        YEARS.append((year, year))

    season = models.IntegerField(
        "Season", default=datetime.datetime.now().year, choices=YEARS
        )
    date = models.DateField("Date")
    mtype = models.TextField("Type", choices=MATCH_TYPE)
    home_or_away = models.TextField("Home or Away", choices=HOME_AWAY)
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


class PlayerMatchAttribute(models.Model):
    player = models.ForeignKey(Player, on_delete=models.SET_NULL, null=True)
    match = models.ForeignKey(Match, on_delete=models.SET_NULL, null=True)
    skill = models.TextField("Skill Set", blank=True, null=True, choices=PLAYER_SKILLS)
    captain = models.BinaryField("Captain", default=False)

    class Meta:
        db_table = "player_match_attributes"

    def __str__(self):
        return f"{self.skill}"
