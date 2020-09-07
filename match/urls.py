from django.urls import path

from .views import MatchAppearances

urlpatterns = [
    # ex: /matches/
    path("appearances/", MatchAppearances.as_view(), name="match-appearances"),
    ]