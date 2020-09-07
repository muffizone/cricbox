from .models import Match
from .tables import MatchTable
import django_filters
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin
from django.db.models import Count


# Create your views here.
class MatchFilter(django_filters.FilterSet):
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


class MatchAppearances(SingleTableMixin, FilterView):
    table_class = MatchTable
    model = Match
    filterset_class = MatchFilter
    template_name = "match/appearances.html"

    def get_queryset(self):
        return Match.objects.values('players').annotate(appearances=Count('players'))

