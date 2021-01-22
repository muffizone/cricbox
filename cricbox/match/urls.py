from .views import AppearancesView, FixtureView

# Django imports
from django.urls import path

urlpatterns = [
    # ex: /match/
    path("appearances/", AppearancesView.as_view(), name="match-appearances-player"),
    path("fixtures/", FixtureView.as_view(), name="fixtures-overview"),
]
