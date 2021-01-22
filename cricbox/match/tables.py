# Cricbox imports
from london_fields.utils import TABLE_ATTRS

# Django third party apps
import django_tables2 as tables


class AppearancesTable(tables.Table):
    players__full_name = tables.Column(verbose_name="Player", linkify=("player-profile", [tables.A("players__id")]))
    appearances = tables.Column()

    class Meta:
        attrs = TABLE_ATTRS
        fields = ("players__full_name", "appearances")


class FixturesTable(tables.Table):
    day = tables.DateColumn(format="D", accessor="date")
    date = tables.Column()
    opposition = tables.Column()
    venue = tables.Column()
    mtype = tables.Column(verbose_name="Type")
    result = tables.Column(
        verbose_name="Result",
        accessor="matchstatistics__result",
        linkify=("match-overview", [tables.A("matchstatistics__id")]),
    )

    class Meta:
        attrs = TABLE_ATTRS
        fields = ("date", "day", "opposition", "venue", "mtype", "result")
