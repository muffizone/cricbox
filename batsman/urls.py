from django.urls import path

from .views import batting_stats, filter_batsman

urlpatterns = [
    # ex: /bowling/
    path("stats/", batting_stats, name="batting-stats"),
    path("<str:full_name>/", filter_batsman, name="batsman-name")
    ]
