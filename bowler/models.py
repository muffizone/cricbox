from django.db import models
from player.models import Player

from match.models import Match

# Create your models here.
class Bowler(models.Model):
    player = models.ForeignKey(Player, on_delete=models.PROTECT, blank=True, null=True)
    overs = models.PositiveSmallIntegerField("Overs", default=0)
    maidens = models.PositiveSmallIntegerField(
        "Maidens", blank=True, null=True, default=0
    )
    runs = models.PositiveIntegerField("Runs", default=0)
    wickets = models.PositiveIntegerField("Wickets", default=0)
    match = models.ForeignKey(Match, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.player.full_name
