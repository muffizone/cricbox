from .models import Bowler
from .tables import BowlersTable, BowlerTable
import django_filters
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin
from london_fields.filters import MatchFilter


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


class BowlersFilter(MatchFilter):
    class Meta:
        model = Bowler
        fields = {
            'match_statistics__match__season': ['exact'],
            'match_statistics__match__mtype': ['exact']
            }


class BowlersView(SingleTableMixin, FilterView):
    filterset_class = BowlersFilter
    template_name = "bowler/bowler.html"
    table_class = BowlersTable
    table_pagination = {
        "per_page": 50
        }

    def get_queryset(self):
        return Bowler.stat_objects.all()


class BowlerView(SingleTableMixin, FilterView):
    table_class = BowlerTable
    filterset_class = BowlerFilter
    template_name = "bowler/single_stats.html"

    def get_queryset(self):
        return Bowler.objects.filter(player__full_name=self.kwargs.get("full_name"))

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context["player"] = self.kwargs.get("full_name")
        return context
