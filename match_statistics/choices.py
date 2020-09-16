from django.db import models

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


class EventFirst(models.TextChoices):
    BATTED = "BAT"
    BOWLED = "BOW"