from django.db import models


class MatchType(models.TextChoices):
    FRIENDLY = "F"
    LEAGUE = "L"
    VPCCL = "V"
    OTHERS = "O"
    TOUR = "T"


class HomeAway(models.TextChoices):
    HOME = "H"
    AWAY = "A"


class PlayerSkills(models.TextChoices):
    BOWLER = "BW"
    BATSMAN = "BT"
    ALL_ROUNDER = "AR"
    WICKET_KEEPER = "WK"
