from django.urls import path

from .views import bowling_stats, filter_bowler, FilterBowlerView

urlpatterns = [
    # ex: /bowling/
    path("stats/", bowling_stats, name="bowling-stats"),
    path("<str:full_name>/", FilterBowlerView.as_view(), name="bowler-name")
    ]
