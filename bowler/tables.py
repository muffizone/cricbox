import django_tables2 as tables
from london_fields.tables import FloatColumn, SummingColumn
from london_fields.utils import TABLE_ATTRS


class BowlersTable(tables.Table):
    player__full_name = tables.Column(linkify=("player-profile", [tables.A("player__full_name")]))
    overs = tables.Column(order_by=("overs", "player__full_name"))
    maidens = tables.Column(order_by=("maidens", "player__full_name"), verbose_name="Md")
    runs = tables.Column(order_by=("runs", "player__full_name"))
    total_wickets = tables.Column(order_by=("total_wickets", "player__full_name"), verbose_name="Wkts")
    average = FloatColumn(order_by=("average", "player__full_name"), verbose_name="Avg")
    strike_rate = FloatColumn(order_by=("strike_rate", "player__full_name"), verbose_name="SR")
    economy = FloatColumn(order_by=("economy", "player__full_name"), verbose_name="Eco")
    matches = tables.Column(order_by=("matches", "player__full_name"), verbose_name="Inn", linkify=("bowling-stats-name", [tables.A("player__full_name")]))
    fours = tables.Column(verbose_name="4w")
    fives = tables.Column(verbose_name="5w")

    class Meta:
        attrs = TABLE_ATTRS
        fields = ("matches", "player__full_name", "overs", "maidens", "runs", "total_wickets", "average", "strike_rate", "economy")
        sequence = ("player__full_name", "matches", "overs", "maidens", "runs", "total_wickets", "average", "strike_rate", "economy")


class BowlerTable(tables.Table):
    runs = SummingColumn()
    maidens = SummingColumn()
    overs = SummingColumn()
    wickets = SummingColumn()
    match = tables.Column(verbose_name="Match",accessor="match_statistics", footer=lambda table: len(table.data))
    economy = tables.Column(orderable=False)
    average = tables.Column(orderable=False)
    strike_rate = tables.Column(orderable=False)
    match_season = tables.Column(accessor="match_statistics__match__season", verbose_name="Season")
    match_type = tables.Column(accessor="match_statistics__match__mtype", verbose_name="Type")
    result = tables.Column(accessor="match_statistics__get_result_display", verbose_name="Result")

    class Meta:
        attrs = TABLE_ATTRS
        sequence = ("match_season", "match", "match_type", "overs", "maidens", "runs", "wickets", "economy", "average", "strike_rate", "result")
        exclude = ("player", "id", "match_statistics")