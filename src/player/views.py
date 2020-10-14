from .models import Player
from .tables import PlayersTable
from batsman.tables import BatsmenTable
from bowler.tables import BowlersTable
from batsman.models import Batsman
from bowler.models import Bowler
from django.views.generic import TemplateView
from django_tables2.views import SingleTableMixin
from match.models import Match


# Create your views here.
class PlayersView(SingleTableMixin, TemplateView):
    template_name = "player/player.html"
    table_class = PlayersTable
    table_pagination = {
        "per_page": 50
        }

    def get_queryset(self):
        return Player.objects.all()


class ProfileView(TemplateView):
    model = Player
    template_name = "player/profile.html"

    def get_context_data(self, **kwargs):
        full_name = kwargs.get("full_name")
        context = super().get_context_data(**kwargs)
        context["batting"] = BatsmenTable(Batsman.stat_objects.filter(player__full_name=full_name), exclude="player")
        context["bowling"] = BowlersTable(Bowler.stat_objects.filter(player__full_name=full_name), exclude="player")
        context["player"] = Player.objects.filter(full_name=full_name)[0]
        context["match_league"] = list(Match.objects.filter(players__full_name=full_name, mtype="L"))
        context["match_friendly"] = list(Match.objects.filter(players__full_name=full_name, mtype="F"))
        context["match_vpccl"] = list(Match.objects.filter(players__full_name=full_name, mtype="V"))
        return context


