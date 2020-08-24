from django.db import models
from player.models import Player
from match.models import Match
from django.db.models import Count, Sum, ExpressionWrapper, F, DecimalField, Max, Q

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

class Statistics(models.Manager):
    def get_queryset(self):
        return super().get_queryset().values('player').annotate(innings=Count('match'), runs_scored=Sum('runs'),
                                                                not_out=Count('how_out',filter=Q(how_out='NO')),
                                                                best=Max('runs'),
                                                                average=ExpressionWrapper(F('runs_scored')/(F('innings')-F('not_out')),
                                                                output_field=DecimalField(max_digits=2, decimal_places=2))).\
                                                                order_by("-runs")


class Batsman(models.Model):
    player = models.ForeignKey(Player, on_delete=models.PROTECT)
    scoring = models.CharField("Scoring", blank=True, null=True, max_length=200)
    how_out = models.CharField(
        "wicket",
        choices=WICKET_TYPES,
        blank=True,
        null=True,
        max_length=10,
    )
    bowler = models.CharField(
        "Name of the opposition team bowler", blank=True, null=True, max_length=20
    )
    runs = models.PositiveIntegerField("Total number of runs")
    match = models.ForeignKey(Match, on_delete=models.CASCADE, blank=True, null=True)
    objects = models.Manager()
    stat_objects = Statistics()

    class Meta:
        ordering = ["player"]
        verbose_name_plural = "Batsmen"

    def __str__(self):
        return self.player.full_name
