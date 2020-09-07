import django_tables2 as tables
from .models import Match


class MatchTable(tables.Table):
    players = tables.Column()
    appearances = tables.Column()

    class Meta:
        attrs = {"class": "table table-striped table-bordered table-hover",
                 "thead": {
                     "class": "thead-light"
                     }
                 }
        model = Match
        template_name = "django_tables2/bootstrap4.html"
        fields = ("players", "appearances")