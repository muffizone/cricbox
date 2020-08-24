import django_tables2 as tables
from django_tables2 import A
from .models import Player


class PlayerTable(tables.Table):
    batting = tables.TemplateColumn('<a href="{% url "batsman-name" record.full_name %}">Batting</a>', verbose_name="",
                                    orderable=False)
    bowling = tables.TemplateColumn('<a href="{% url "bowler-name" record.full_name %}">Bowling</a>', verbose_name="",
                                    orderable=False)

    class Meta:
        model = Player
        template_name = "django_tables2/bootstrap.html"
