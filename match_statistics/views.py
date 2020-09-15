from django.shortcuts import render
from .tables import SeasonTable, OppositionTable, VenuesTable, BattingTable, BowlingTable
import django_filters
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin
from django.db.models import Count, Q, ExpressionWrapper, F, DecimalField, FloatField
from .models import MatchStatistics
from django_tables2 import MultiTableMixin
from django.views.generic.base import TemplateView
from match.views import FixturesFilter


# Create your views here.
class OppositionFilter(django_filters.FilterSet):

    season = django_filters.RangeFilter(field_name='match__season')

    class Meta:
        model = MatchStatistics
        fields = {
                'match__mtype': ['exact'],
                'match__home_or_away': ['exact'],
                'match__venue': ['exact'],
            }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.filters['match__mtype'].label = 'Type'
        self.filters['match__home_or_away'].label = 'HomeorAway'
        self.filters['match__venue'].label = 'Venue'


class VenueFilter(django_filters.FilterSet):

    season = django_filters.RangeFilter(field_name='match__season')

    class Meta:
        model = MatchStatistics
        fields = {
                'match__mtype': ['exact'],
                'match__home_or_away': ['exact'],
                'match__opposition': ['exact'],
            }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.filters['match__mtype'].label = 'Type'
        self.filters['match__home_or_away'].label = 'HomeorAway'
        self.filters['match__opposition'].label = 'Opposition'


class SeasonView(SingleTableMixin, FilterView):
    table_class = SeasonTable
    model = MatchStatistics
    filterset_class = FixturesFilter
    template_name = "match/fixtures.html"

    def get_queryset(self):
        won = Count('match', filter=Q(result='W'))
        loss = Count('match', filter=Q(result='L'))
        no_result = Count('match', filter=Q(result='N'))
        draw = Count('match', filter=Q(result='D'))

        return self.model.objects.values('match__season').annotate(played=Count('match'), won=won, loss=loss,
                                                                        no_result=no_result, draw=draw,
                                                                        win_percent=ExpressionWrapper(F('won')/F('played'),
                                                                                                      output_field=FloatField()))


class OppositionView(SingleTableMixin, FilterView):
    table_class = OppositionTable
    model = MatchStatistics
    filterset_class = OppositionFilter
    template_name = "match/fixtures.html"

    def get_queryset(self):
        won = Count('match', filter=Q(result='W'))
        loss = Count('match', filter=Q(result='L'))
        no_result = Count('match', filter=Q(result='N'))
        draw = Count('match', filter=Q(result='D'))

        return self.model.objects.values('match__opposition').annotate(played=Count('match'), won=won, loss=loss,
                                                                        no_result=no_result, draw=draw,
                                                                        win_percent=ExpressionWrapper(F('won')/F('played'),
                                                                                                      output_field=DecimalField()))


class VenuesView(SingleTableMixin, FilterView):
    table_class = VenuesTable
    model = MatchStatistics
    filterset_class = VenueFilter
    template_name = "match/fixtures.html"

    def get_queryset(self):
        won = Count('match', filter=Q(result='W'))
        loss = Count('match', filter=Q(result='L'))
        no_result = Count('match', filter=Q(result='N'))
        draw = Count('match', filter=Q(result='D'))

        return self.model.objects.values('match__venue').annotate(played=Count('match'), won=won, loss=loss,
                                                                        no_result=no_result, draw=draw,
                                                                        win_percent=ExpressionWrapper(F('won')/F('played'),
                                                                                                      output_field=DecimalField()))


class MatchView(MultiTableMixin, TemplateView):
    template_name = "match_statistics/match_overview.html"

    def get_queryset(self, **kwargs):
        return MatchStatistics.objects.filter(id=self.kwargs.get("id"))

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context["match_stats"] = self.get_queryset(**kwargs)[0]
        return context

    def get_tables(self, **kwargs):
        match_stats = self.get_queryset(**kwargs)
        return [
                BowlingTable(match_stats[0].get_bowlers()),
                BattingTable(match_stats[0].get_batsman())
        ]

