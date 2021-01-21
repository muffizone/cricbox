from django.urls import path

from .views import PlayersView, ProfileView

# path: players/
urlpatterns = [
    path("", PlayersView.as_view(), name="players"),
    path("profiles/<int:player_id>/", ProfileView.as_view(), name="player-profile"),
]

