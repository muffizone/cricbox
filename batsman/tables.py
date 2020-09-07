import django_tables2 as tables
from .models import Batsman
from london_fields.tables import FloatColumn, SummingColumn


class BatsmanTable(tables.Table):
    innings = tables.Column(order_by=("innings", "player"))
    runs_scored = tables.Column(order_by=("runs_scored", "player"))
    not_out = tables.Column(order_by=("not_out", "player"))
    best = tables.Column(order_by=("best", "player"))
    average = FloatColumn(order_by=("average", "player"))

    class Meta:
        model = Batsman
        template_name = "django_tables2/bootstrap.html"
        fields = ("player", "innings", "runs_scored", "not_out", "best", "average")


class SingleBatsman(tables.Table):
    runs = SummingColumn()
    match = tables.Column(footer=lambda table: len(table.data), accessor="match_statistics", verbose_name="match")
    match_season = tables.Column(accessor="match_statistics__match__season", verbose_name="Season")
    match_type = tables.Column(accessor="match_statistics__match__mtype", verbose_name="Type")

    class Meta:
        attrs = {"class": "table table-striped table-bordered table-hover",
                 "thead": {
                     "class": "thead-light"
                     }
                 }
        sequence = ("match_season", "match", "match_type", "scoring", "how_out", "bowler", "runs")
        model = Batsman
        exclude = ("player", "id")
        template_name = "django_tables2/bootstrap4.html"