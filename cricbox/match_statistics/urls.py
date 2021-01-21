from django.urls import path

from .views import SeasonView, OppositionView, VenuesView, MatchView

urlpatterns = [
    # ex: /season/
    path("overview/", SeasonView.as_view(), name="season-overview"),
    path("opposition/", OppositionView.as_view(), name="opposition-overview"),
    path("venues/", VenuesView.as_view(), name="venues-overview"),
    path("match/<int:id>/", MatchView.as_view(), name="match-overview")
    ]