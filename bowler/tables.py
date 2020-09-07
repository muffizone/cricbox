import django_tables2 as tables
from london_fields.tables import FloatColumn, SummingColumn
from .models import Bowler


class BowlerTable(tables.Table):
    overs = tables.Column(order_by=("overs", "player"))
    maidens = tables.Column(order_by=("maidens", "player"))
    runs = tables.Column(order_by=("runs", "player"))
    wickets = tables.Column(order_by=("wickets", "player"))
    average = FloatColumn(order_by=("average", "player"))
    strike_rate = FloatColumn(order_by=("strike_rate", "player"))
    economy = FloatColumn(order_by=("economy", "player"))
    matches = tables.Column(order_by=("matches", "player"))
    # player = tables.Column(linkify=True)

    class Meta:
        model = Bowler
        template_name = "django_tables2/bootstrap.html"
        fields = ("player", "overs", "maidens", "runs", "wickets", "average", "strike_rate", "economy","matches")


class SingleBowler(tables.Table):
    runs = SummingColumn()
    maidens = SummingColumn()
    overs = SummingColumn()
    wickets = SummingColumn()
    match = tables.Column(footer=lambda table: len(table.data))
    economy = tables.Column(orderable=False)
    average = tables.Column(orderable=False)
    strike_rate = tables.Column(orderable=False)
    match_season = tables.Column(accessor="match__season", verbose_name="Season")
    match_type = tables.Column(accessor="match__mtype", verbose_name="Type")

    class Meta:
        attrs = {"class": "table table-striped table-bordered table-hover",
                 "thead": {
                     "class": "thead-light"
                     }
                 }
        sequence = ("match_season", "match", "match_type", "overs", "maidens", "runs", "wickets", "economy", "average", "strike_rate")
        model = Bowler
        exclude = ("player", "id")
        template_name = "django_tables2/bootstrap4.html"