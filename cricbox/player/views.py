from .models import Player
from .tables import PlayersTable
from batsman.tables import BatsmenTable
from bowler.tables import BowlersTable
from batsman.models import Batsman
from bowler.models import Bowler
from django.views.generic import TemplateView
from django_tables2.views import SingleTableMixin
from match.models import Match
from london_fields.utils import INVALID_PLAYERS


# Create your views here.
class PlayersView(SingleTableMixin, TemplateView):
    template_name = "player/player.html"
    table_class = PlayersTable
    table_pagination = {"per_page": 50}

    def get_queryset(self):
        return Player.objects.exclude(INVALID_PLAYERS).all().order_by("first_name")


class ProfileView(TemplateView):
    model = Player
    template_name = "player/profile.html"

    def get_context_data(self, **kwargs):
        player_id = self.kwargs.get("player_id")
        context = super().get_context_data(**kwargs)
        context["batting"] = BatsmenTable(
            Batsman.stat_objects.filter(player_id=player_id), exclude="player"
        )
        context["bowling"] = BowlersTable(
            Bowler.stat_objects.filter(player_id=player_id), exclude="player"
        )
        context["player"] = Player.objects.filter(id=player_id)[0]
        context["match_league"] = list(
            Match.objects.filter(players__id=player_id, mtype__name="League")
        )
        context["match_friendly"] = list(
            Match.objects.filter(players__id=player_id, mtype__name="Friendly")
        )
        context["match_vpccl"] = list(
            Match.objects.filter(players__id=player_id, mtype__name="VPCCL")
        )
        return context
