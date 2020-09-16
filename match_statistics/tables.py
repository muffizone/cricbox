import django_tables2 as tables
from .models import MatchStatistics
from london_fields.tables import FloatColumn, SummingColumn
from django.db.models import F, ExpressionWrapper, DecimalField
from match.models import Match


class SeasonTable(tables.Table):
    played = tables.Column(verbose_name="P")
    won = tables.Column(verbose_name="W")
    draw = tables.Column(verbose_name="D")
    loss = tables.Column(verbose_name="L")
    no_result = tables.Column(verbose_name="N/R")
    win_percent = FloatColumn(verbose_name="%")

    class Meta:
        attrs = {"class": "table table-striped table-bordered table-hover",
                 "thead": {
                     "class": "thead-light"
                     }
                 }
        model = MatchStatistics
        template_name = "django_tables2/bootstrap4.html"
        fields = ("match__season", "played", "won", "draw", "loss", "no_result", "win_percent")


class OppositionTable(tables.Table):
    played = tables.Column(verbose_name="P")
    won = tables.Column(verbose_name="W")
    draw = tables.Column(verbose_name="D")
    loss = tables.Column(verbose_name="L")
    no_result = tables.Column(verbose_name="N/R")
    win_percent = FloatColumn(verbose_name="%")

    class Meta:
        attrs = {"class": "table table-striped table-bordered table-hover",
                 "thead": {
                     "class": "thead-light"
                     }
                 }
        model = MatchStatistics
        template_name = "django_tables2/bootstrap4.html"
        fields = ("match__opposition", "played", "won", "loss", "no_result", "draw", "win_percent")


class VenuesTable(tables.Table):
    played = tables.Column(verbose_name="P")
    won = tables.Column(verbose_name="W")
    draw = tables.Column(verbose_name="D")
    loss = tables.Column(verbose_name="L")
    no_result = tables.Column(verbose_name="N/R")
    win_percent = FloatColumn(verbose_name="%")

    class Meta:
        attrs = {"class": "table table-striped table-bordered table-hover",
                 "thead": {
                     "class": "thead-light"
                     }
                 }
        model = MatchStatistics
        template_name = "django_tables2/bootstrap4.html"
        fields = ("match__venue", "played", "won", "loss", "no_result", "draw", "win_percent")


# class FixturesTable(tables.Table):
#     day = tables.DateColumn(format='D', accessor="date")
#     date = tables.Column()
#     opposition = tables.Column()
#     venue = tables.Column()
#     mtype = tables.Column(verbose_name="Type", accessor="get_mtype_display")
#     result = tables.Column(verbose_name="Result", accessor="matchstatistics__get_result_display", linkify=("match-overview", [tables.A("matchstatistics__id")]))
#
#     class Meta:
#         attrs = {"class": "table table-striped table-bordered table-hover",
#                  "thead": {
#                      "class": "thead-light"
#                      }
#                  }
#         model = Match
#         template_name = "django_tables2/bootstrap4.html"
#         fields = ("date", "day", "opposition", "venue", "mtype", "result")


class BowlingTable(tables.Table):
    player = tables.Column(verbose_name="Name")
    overs = tables.Column(verbose_name="O")
    maidens = tables.Column(verbose_name="M")
    runs = tables.Column(verbose_name="R")
    wickets = tables.Column(verbose_name="W")
    economy = tables.Column(verbose_name="Eco", orderable=False)
    average = tables.Column(verbose_name="Avg", orderable=False)
    strike_rate = tables.Column(verbose_name="S.R", orderable=False)


    class Meta:
        attrs = {"class": "table table-striped table-bordered table-hover",
                 "thead": {
                     "class": "thead-light"
                     }
                 }
        template_name = "django_tables2/bootstrap4.html"
        fields = ("player", "overs", "maidens", "runs", "wickets", "economy", "average", "strike_rate")


class BattingTable(tables.Table):
    player = tables.Column(verbose_name="Name")
    scoring = tables.Column()
    how_out = tables.Column(verbose_name="How Out")
    bowler = tables.Column()
    runs = SummingColumn()

    class Meta:
        attrs = {"class": "table table-striped table-bordered table-hover",
                 "thead": {
                     "class": "thead-light"
                     }
                 }
        template_name = "django_tables2/bootstrap4.html"
        fields = ("player", "scoring", "how_out", "bowler", "runs")