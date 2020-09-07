from django.urls import path

from .views import batting_stats, FilterBatsmanView

urlpatterns = [
    # ex: /batting/
    path("stats/", batting_stats, name="batting-stats"),
    path("<str:full_name>/", FilterBatsmanView.as_view(), name="batsman-name")
    ]
