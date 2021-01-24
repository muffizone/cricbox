# Cricbox imports
from cricbox.utils import TABLE_ATTRS

# Django third party apps
import django_tables2 as tables


class Scorecard(tables.Table):
    name = tables.Column(orderable=False)
    first_innings = tables.Column(orderable=False)
    second_innings = tables.Column(orderable=False)

    class Meta:
        attrs = TABLE_ATTRS


class HonoursTable(tables.Table):
    name = tables.Column(linkify=("player-profile", [tables.A("name_id")]))
    season = tables.Column()

    class Meta:
        attrs = TABLE_ATTRS


class NotablePerformancesTable(tables.Table):
    player = tables.Column(linkify=("player-profile", [tables.A("player_id")]))
    runs = tables.Column()
    wickets = tables.Column()
    season = tables.Column(accessor="match_statistics__match__season")
    match = tables.Column(accessor="match_statistics__match")
    mtype = tables.Column(accessor="match_statistics__match__mtype")
    result = tables.Column(accessor="match_statistics__result")

    class Meta:
        attrs = TABLE_ATTRS


class VeteransTable(tables.Table):
    first_name = tables.Column(verbose_name="Veteran", linkify=("player-profile", [tables.A("id")]))
    member_since = tables.Column(verbose_name="Since")

    def render_first_name(self, value, record):
        return f"{value} {record.last_name}"

    class Meta:
        attrs = TABLE_ATTRS


class BestPlayer(tables.Table):
    name = tables.Column(linkify=("player-profile", [tables.A("id")]))
    season = tables.Column()
    total = tables.Column()

    class Meta:
        attrs = TABLE_ATTRS
