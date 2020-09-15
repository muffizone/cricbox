import django_tables2 as tables
from london_fields.utils import TABLE_ATTRS


class PlayersTable(tables.Table):
    batting = tables.TemplateColumn('<a href="{% url "batsman-stats" record.full_name %}">Batting</a>', verbose_name="")
    bowling = tables.TemplateColumn('<a href="{% url "bowling-stats-name" record.full_name %}">Bowling</a>', verbose_name="")
    member_since = tables.DateColumn(verbose_name="Joined")
    playing_role = tables.Column(verbose_name="Role")
    batting_style = tables.Column(verbose_name="Bat")
    bowling_style = tables.Column(verbose_name="Bowl")
    full_name = tables.Column(verbose_name="Name", linkify=("player-profile", [tables.A("full_name")]))

    class Meta:
        attrs = TABLE_ATTRS
        template_name = "django_tables2/bootstrap4.html"
        sequence = ("full_name", "member_since", "playing_role", "batting_style", "bowling_style",
                    "batting", "bowling")
