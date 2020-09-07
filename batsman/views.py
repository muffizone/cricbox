from django.shortcuts import render
from .models import Batsman
from django_tables2 import RequestConfig
from .tables import BatsmanTable, SingleBatsman
import django_filters
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin


# filters
class BatsmanFilter(django_filters.FilterSet):
    class Meta:
        model = Batsman
        fields = {
            'match_statistics__match__season': ['exact'],
            'match_statistics__match__mtype': ['exact'],
            'how_out': ['exact'],
            'runs': ['gte'],
            }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.filters['match_statistics__match__season'].label = 'Season'
        self.filters['match_statistics__match__mtype'].label = 'Type'
        self.filters['how_out'].label = 'Wickets'
        self.filters['runs__gte'].label = 'Runs'


# Create your views here.
def batting_stats(request):
    table = BatsmanTable(Batsman.stat_objects.all())
    RequestConfig(request, paginate={"per_page": 50}).configure(table)
    return render(request, "batsman/batsman.html", {"table": table})


class FilterBatsmanView(SingleTableMixin, FilterView):
    table_class = SingleBatsman
    model = Batsman
    filterset_class = BatsmanFilter
    template_name = "batsman/single_stats.html"

    def get_queryset(self):
        return Batsman.objects.filter(player__full_name=self.kwargs.get("full_name"))

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context["player"] = self.kwargs.get("full_name")
        return context
