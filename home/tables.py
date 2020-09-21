import django_tables2 as tables
from london_fields.utils import TABLE_ATTRS


class Scorecard(tables.Table):
    name = tables.Column(orderable=False)
    first_innings = tables.Column(orderable=False)
    second_innings = tables.Column(orderable=False)

    class Meta:
        attrs = TABLE_ATTRS


class HonoursTable(tables.Table):
    name = tables.Column(linkify=("player-profile", [tables.A("name")]))
    season = tables.Column()

    class Meta:
        attrs = TABLE_ATTRS


class NotablePerformancesTable(tables.Table):
    player = tables.Column()
    runs = tables.Column()
    wickets = tables.Column()
    season = tables.Column(accessor="match_statistics__match__season")
    match = tables.Column(accessor="match_statistics__match")
    mtype = tables.Column(accessor="match_statistics__match__mtype")
    result = tables.Column(accessor="match_statistics__result")

    class Meta:
        attrs = TABLE_ATTRS


class VeteransTable(tables.Table):
    full_name = tables.Column(verbose_name="Veteran")
    member_since = tables.Column(verbose_name="Since")

    class Meta:
        attrs = TABLE_ATTRS
