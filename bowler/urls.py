from django.urls import path

from .views import bowling_stats, filter_bowler

urlpatterns = [
    # ex: /bowling/
    path("stats/", bowling_stats, name="bowling-stats"),
    path("<str:full_name>/", filter_bowler, name="bowler-name")
    ]
