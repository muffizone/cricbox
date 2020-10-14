from django.urls import path

from .views import BowlerView, BowlersView

urlpatterns = [
    # ex: /bowling/
    path("stats/", BowlersView.as_view(), name="bowling-stats-all"),
    path("<str:full_name>/", BowlerView.as_view(), name="bowling-stats-name")
    ]
