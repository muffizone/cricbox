from django.urls import path
from .views import home, about, history, links, honours, handbook, match_manager, stats

urlpatterns = [
    path("", home, name="site-home"),
    path("about/", about, name="site-about"),
    path("history/", history, name="site-history"),
    path("links/", links, name="site-links"),
    path("honours/", honours, name="site-honours"),
    path("handbook/", handbook, name="site-handbook"),
    path("match-manager/", match_manager, name="site-match_manager"),
    path("stats/", stats, name="site-stats")
]