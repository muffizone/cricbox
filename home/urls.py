from django.urls import path
from .views import home, about, history, links, handbook, match_manager, stats, PositionsView, PerformersView

urlpatterns = [
    path("", home, name="site-home"),
    path("about/", about, name="site-about"),
    path("history/", history, name="site-history"),
    path("links/", links, name="site-links"),
    path("honours/positions", PositionsView.as_view(), name="site-positions"),
    path("honours/performers", PerformersView.as_view(), name="site-performers"),
    path("handbook/", handbook, name="site-handbook"),
    path("match-manager/", match_manager, name="site-match_manager"),
    path("stats/", stats, name="site-stats")
]