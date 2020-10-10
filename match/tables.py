import django_tables2 as tables
from london_fields.utils import TABLE_ATTRS


class AppearancesTable(tables.Table):
    players__full_name = tables.Column(verbose_name="Player", linkify=("player-profile", [tables.A("players__full_name")]))
    appearances = tables.Column()

    class Meta:
        attrs = TABLE_ATTRS
        fields = ("players__full_name", "appearances")


class FixturesTable(tables.Table):
    day = tables.DateColumn(format='D', accessor="date")
    date = tables.Column()
    opposition = tables.Column()
    venue = tables.Column()
    mtype = tables.Column(verbose_name="Type", accessor="get_mtype_display")
    result = tables.Column(verbose_name="Result", accessor="matchstatistics__get_result_display",
                           linkify=("match-overview", [tables.A("matchstatistics__id")]))

    class Meta:
        attrs = TABLE_ATTRS
        fields = ("date", "day", "opposition", "venue", "mtype", "result")

