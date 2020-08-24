from django.shortcuts import render
from .models import Bowler
from django_tables2 import RequestConfig
from .tables import BowlerTable, SingleBowler


# Create your views here.
def bowling_stats(request):
    table = BowlerTable(Bowler.stat_objects.all())
    RequestConfig(request, paginate={"per_page": 50}).configure(table)
    return render(request, "bowler/bowler.html", {"table": table})


def filter_bowler(request, full_name):
    table = SingleBowler(Bowler.objects.filter(player__full_name=full_name))
    RequestConfig(request, paginate={"per_page": 50}).configure(table)
    return render(request, "bowler/single_stats.html", {"table": table, "player": full_name})
