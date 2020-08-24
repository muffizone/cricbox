from .models import Player
from django.shortcuts import render
from django_tables2 import RequestConfig
from .tables import PlayerTable
from bowler.models import Bowler


# Create your views here.
def index(request):
    table = PlayerTable(Player.objects.all())
    RequestConfig(request, paginate={"per_page": 50}).configure(table)
    return render(request, "player/player.html", {"table": table})



