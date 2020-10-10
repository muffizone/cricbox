from django.db import models
from match.models import Match
from .choices import RESULT, EVENT_FIRST


class MatchStatistics(models.Model):
    match = models.OneToOneField(Match, on_delete=models.CASCADE)
    result = models.TextField("Result", choices=RESULT)
    report = models.TextField("Report", blank=True, null=True)
    london_fields_overs = models.PositiveSmallIntegerField("London Fields Overs")
    london_fields_score = models.PositiveSmallIntegerField("London Fields Score",)
    london_fields_wickets = models.PositiveSmallIntegerField(
        "London Fields Wickets"
    )
    opposition_score = models.PositiveSmallIntegerField("Opposition score")
    opposition_wickets = models.PositiveSmallIntegerField("Opposition Wickets")
    opposition_overs = models.PositiveSmallIntegerField("Opposition overs")
    london_fields_first_event = models.TextField(choices=EVENT_FIRST)

    def get_bowlers(self):
        return self.bowler_set.get_queryset()

    def get_batsman(self):
        return self.batsman_set.get_queryset()

    class Meta:
        ordering = ("match", )
        db_table = "matches_statistics"
        verbose_name_plural = "Match Statistics"

    def __str__(self):
        return f"{self.match}"
