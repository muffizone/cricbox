from .models import Batsman
from .tables import BatsmenTable, BatsmanTable
import django_filters
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin
from london_fields.filters import MatchFilter


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


class BatsmenFilter(MatchFilter):
    class Meta:
        model = Batsman
        fields = {
            'match_statistics__match__season': ['exact'],
            'match_statistics__match__mtype': ['exact']
            }


# Create your views here.
class BatsmenView(SingleTableMixin, FilterView):
    filterset_class = BatsmenFilter
    template_name = "batsman/batsman.html"
    table_class = BatsmenTable
    table_pagination = {
        "per_page": 50
        }

    def get_queryset(self):
        return Batsman.stat_objects.all()


class BatsmanView(SingleTableMixin, FilterView):
    table_class = BatsmanTable
    filterset_class = BatsmanFilter
    template_name = "batsman/single_stats.html"

    def get_queryset(self):
        return Batsman.objects.filter(player__full_name=self.kwargs.get("full_name"))

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context["player"] = self.kwargs.get("full_name")
        return context
