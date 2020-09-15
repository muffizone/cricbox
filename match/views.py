from .models import Match
from .tables import AppearancesTable, FixturesTable
import django_filters
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin
from django.db.models import Count


# Create your views here.
class AppearancesFilter(django_filters.FilterSet):
    class Meta:
        model = Match
        fields = {
                'season': ['exact'],
                'mtype': ['exact'],
                'home_or_away': ['exact'],
                'opposition': ['exact'],
                'venue': ['exact'],
            }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.filters['season'].label = 'Season'
        self.filters['mtype'].label = 'Type'
        self.filters['home_or_away'].label = 'HomeorAway'
        self.filters['opposition'].label = 'Opposition'
        self.filters['venue'].label = 'Venue'


class FixturesFilter(django_filters.FilterSet):
    class Meta:
        model = Match
        fields = {
                'mtype': ['exact'],
                'home_or_away': ['exact'],
                'opposition': ['exact'],
                'venue': ['exact'],
            }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.filters['mtype'].label = 'Type'
        self.filters['home_or_away'].label = 'HomeorAway'
        self.filters['opposition'].label = 'Opposition'
        self.filters['venue'].label = 'Venue'


class AppearancesView(SingleTableMixin, FilterView):
    table_class = AppearancesTable
    model = Match
    filterset_class = AppearancesFilter
    template_name = "match/appearances.html"

    def get_queryset(self):
        return Match.objects.values('players').annotate(appearances=Count('players'))


class FixtureView(SingleTableMixin, FilterView):
    table_class = FixturesTable
    model = Match
    filterset_class = FixturesFilter
    template_name = "match/fixtures.html"
