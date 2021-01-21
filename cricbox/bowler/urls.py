from django.urls import path

from .views import BowlerView, BowlersView

urlpatterns = [
    # ex: /bowling/
    path("stats/", BowlersView.as_view(), name="bowling-stats-all"),
    path("<int:id>/", BowlerView.as_view(), name="bowling-stats-name"),
]
