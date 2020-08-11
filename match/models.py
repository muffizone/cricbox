from django.db import models

from venue.models import Venue
from opposition.models import Opposition

# from bowler.models import Bowler
import datetime

# Create your models here.


class Result(models.TextChoices):
    WON = "W"
    LOST = "L"
    NO_RESULT = "N"
    DRAWN = "T"
    ABANDONED = "A"
    WALK_OVER = "WO"
    POSTPONDED = "P"
    RAINED_OFF = "R"
    UNKNOWN = "U"


class MatchType(models.TextChoices):
    FRIENDLY = "F"
    LEAGUE = "L"
    VPCCL = "V"
    OTHERS = "O"


class HomeAway(models.TextChoices):
    HOME = "H"
    AWAY = "A"


class EventFirst(models.TextChoices):
    BATTED = "BAT"
    BOWLED = "BOW"


class Match(models.Model):
    YEARS = []
    for year in range(1997, datetime.datetime.now().year + 1):
        YEARS.append((year, year))

    season = models.IntegerField(
        "Season year", default=datetime.datetime.now().year, choices=YEARS
    )
    played = models.DateField("Match date")
    result = models.TextField("Game result", choices=Result.choices)
    mtype = models.TextField("Match Type", choices=MatchType.choices)
    home_or_away = models.TextField("Home or Away", choices=HomeAway.choices)
    remarks = models.TextField(
        "Extra comments or remarks about the summary", blank=True, null=True
    )
    report = models.TextField("Match report", blank=True, null=True)
    london_fields_score = models.PositiveSmallIntegerField("London Fields Score",)
    london_fields_wickets = models.PositiveSmallIntegerField(
        "London Fields Fallen Wickets"
    )
    london_fields_overs = models.PositiveSmallIntegerField("London Fields Overs used")
    other_team_score = models.PositiveSmallIntegerField("Other team score")
    other_team_wickets = models.PositiveSmallIntegerField("Other team Fallen Wickets")
    other_team_overs = models.PositiveSmallIntegerField("Other team overs used")
    london_fields_first_event = models.TextField(choices=EventFirst.choices)
    opposition = models.ForeignKey(
        Opposition, on_delete=models.PROTECT, blank=True, null=True
    )
    venue = models.ForeignKey(Venue, on_delete=models.PROTECT, blank=True, null=True)
    # bowler = models.ForeignKey(Bowler, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"London Fields vs {self.opposition} at {self.venue} on {self.played}"

