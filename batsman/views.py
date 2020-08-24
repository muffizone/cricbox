from django.shortcuts import render
from .models import Batsman
from django_tables2 import RequestConfig
from .tables import BatsmanTable, SingleBatsman


# Create your views here.
def batting_stats(request):
    table = BatsmanTable(Batsman.stat_objects.all())
    RequestConfig(request, paginate={"per_page": 50}).configure(table)
    return render(request, "batsman/batsman.html", {"table": table})


def filter_batsman(request, full_name):
    table = SingleBatsman(Batsman.objects.filter(player__full_name=full_name))
    RequestConfig(request, paginate={"per_page": 50}).configure(table)
    return render(request, "batsman/single_stats.html", {"table": table, "player": full_name})

