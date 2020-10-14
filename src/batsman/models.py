from django.db import models
from player.models import Player
from match.models import Match
from match_statistics.models import MatchStatistics
from django.db.models import Count, Sum, ExpressionWrapper, F, DecimalField, Max, Q
from .choices import WICKET_TYPES
from london_fields.utils import FIFTIES, HUNDREDS

class Statistics(models.Manager):
    def get_queryset(self):
        return super().get_queryset().values('player__full_name').annotate(innings=Count('match_statistics'), runs_scored=Sum('runs'),
                                                                not_out=Count('how_out', filter=Q(how_out='NO')),
                                                                highest=Max('runs'),
                                                                average=ExpressionWrapper(
                                                                    F('runs_scored') / (F('innings') - F('not_out')),
                                                                    output_field=DecimalField(max_digits=2,
                                                                                              decimal_places=2)),
                                                                fifties=Count('runs', filter=FIFTIES),
                                                                hundreds=Count('runs', filter=HUNDREDS)). \
            order_by("-runs_scored")


class Batsman(models.Model):
    player = models.ForeignKey(Player, on_delete=models.PROTECT)
    scoring = models.CharField("Scoring", blank=True, max_length=200)
    runs = models.PositiveIntegerField("Runs", blank=True)
    how_out = models.CharField(
        "wicket",
        choices=WICKET_TYPES,
        blank=True,
        max_length=10,
        )
    bowler = models.CharField(
        "Bowler", blank=True, max_length=20
        )

    match_statistics = models.ForeignKey(MatchStatistics, on_delete=models.PROTECT)
    objects = models.Manager()
    stat_objects = Statistics()

    class Meta:
        ordering = ["player"]
        verbose_name_plural = "Batsmen"
        db_table = "batsmen"

    def __str__(self):
        return self.player.full_name
