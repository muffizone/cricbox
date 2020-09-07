from django.shortcuts import render
from .models import Bowler
from django_tables2 import RequestConfig
from .tables import BowlerTable, SingleBowler
import django_filters
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin


class BowlerFilter(django_filters.FilterSet):
    class Meta:
        model = Bowler
        fields = {
            'match_statistics__match__season': ['exact'],
            'match_statistics__match__mtype': ['exact'],
            'wickets': ['gte'],
            'runs': ['gte'],
            }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.filters['match_statistics__match__season'].label = 'Season'
        self.filters['match_statistics__match__mtype'].label = 'Type'
        self.filters['wickets__gte'].label = 'Wickets'
        self.filters['runs__gte'].label = 'Runs'


# Create your views here.
def bowling_stats(request):
    table = BowlerTable(Bowler.stat_objects.all())
    RequestConfig(request, paginate={"per_page": 50}).configure(table)
    return render(request, "bowler/bowler.html", {"table": table})


def filter_bowler(request, full_name):
    table = SingleBowler(Bowler.objects.filter(player__full_name=full_name))
    RequestConfig(request, paginate={"per_page": 50}).configure(table)
    return render(request, "bowler/single_stats.html", {"table": table, "player": full_name})


class FilterBowlerView(SingleTableMixin, FilterView):
    table_class = SingleBowler
    model = Bowler
    filterset_class = BowlerFilter
    template_name = "bowler/single_stats.html"

    def get_queryset(self):
        return Bowler.objects.filter(player__full_name=self.kwargs.get("full_name"))

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context["player"] = self.kwargs.get("full_name")
        return context
