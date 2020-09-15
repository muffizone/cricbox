from django.urls import path

from .views import PlayersView, ProfileView

# path: players/
urlpatterns = [path("", PlayersView.as_view(), name="players"),
               path("profiles/<str:full_name>", ProfileView.as_view(), name="player-profile")
               ]

