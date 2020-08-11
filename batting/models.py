from django.db import models
from player.models import Player

WICKET_TYPES = (
    ("C", "CAUGHT"),
    ("BOW", "BOWLED"),
    ("RO", "RUN OUT"),
    ("RETH", "RETIRED HURT"),
    ("RETO", "RETIRED OUT"),
    ("CBOWL", "CAUGHT & BOWLED"),
    ("CBEH", "CAUGHT BEHIND"),
    ("DNB", "DID NOT BAT"),
    ("NO", "NOT OUT"),
    ("HB", "HANDLED BALL"),
    ("HBT", "HIT BALL TWICE"),
    ("HW", "HIT WICKET"),
    ("LBW", "LBW"),
    ("OF", "OBSTRUCTING FIELD"),
    ("S", "STUMPED"),
    ("TO", "TIMED OUT"),
    ("U", "UNKNOWN"),
)

# Create your models here.
class Batting(models.Model):
    player = models.ForeignKey(Player, on_delete=models.PROTECT)
    scoring = models.CharField("Scoring", blank=True, null=True, max_length=200)
    how_out = models.CharField(
        "How did the batsmen got out",
        choices=WICKET_TYPES,
        blank=True,
        null=True,
        max_length=10,
    )
    bowler = models.CharField(
        "Name of the opposition team bowler", blank=True, null=True, max_length=50
    )
    runs = models.PositiveIntegerField("Total number of runs")

