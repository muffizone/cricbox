from django.urls import path

from .views import AppearancesView, FixtureView

urlpatterns = [
    # ex: /match/
    path("appearances/", AppearancesView.as_view(), name="match-appearances-player"),
    path("fixtures/", FixtureView.as_view(), name="fixtures-overview"),
]

