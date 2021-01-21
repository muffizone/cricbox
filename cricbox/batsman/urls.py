from django.urls import path

from .views import BatsmanView, BatsmenView

urlpatterns = [
    # ex: /batting/
    path("stats/", BatsmenView.as_view(), name="batsmen-stats"),
    path("<int:id>/", BatsmanView.as_view(), name="batsman-stats"),
]
