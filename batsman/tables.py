import django_tables2 as tables
from .models import Batsman
from london_fields.tables import FloatColumn, SummingColumn
from london_fields.utils import TABLE_ATTRS


class BatsmenTable(tables.Table):
    player = tables.Column(linkify=("player-profile", [tables.A("player")]))
    innings = tables.Column(order_by=("innings", "player"), verbose_name="Inns", linkify=("batsman-stats",
                                                                                          [tables.A("player")]))
    runs_scored = tables.Column(order_by=("runs_scored", "player"), verbose_name="Runs")
    not_out = tables.Column(order_by=("not_out", "player"), verbose_name="NO")
    highest = tables.Column(order_by=("best", "player"), verbose_name="HS")
    average = FloatColumn(order_by=("average", "player"), verbose_name="Avg")
    fifties = tables.Column(verbose_name="50")
    hundreds = tables.Column(verbose_name="100")

    class Meta:
        attrs = TABLE_ATTRS
        model = Batsman
        fields = ("player", "innings", "runs_scored", "not_out", "highest", "average", "fifties", "hundreds")


class BatsmanTable(tables.Table):
    runs = SummingColumn()
    match = tables.Column(footer=lambda table: len(table.data), accessor="match_statistics", verbose_name="Match")
    match_season = tables.Column(accessor="match_statistics__match__season", verbose_name="Season")
    match_type = tables.Column(accessor="match_statistics__match__mtype", verbose_name="Type")
    result = tables.Column(accessor="match_statistics__get_result_display", verbose_name="Result")

    class Meta:
        attrs = TABLE_ATTRS
        sequence = ("match_season", "match", "match_type", "scoring", "how_out", "bowler", "runs", "result")
        model = Batsman
        exclude = ("player", "id", "match_statistics")
