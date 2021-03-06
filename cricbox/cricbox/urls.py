"""cricbox URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from .sitemaps import StaticViewSitemap

# Django imports
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("home.urls")),
    path("players/", include("player.urls")),
    path("bowling/", include("bowler.urls")),
    path("batting/", include("batsman.urls")),
    path("match/", include("match.urls")),
    path("season/", include("match_statistics.urls")),
    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": {"static": StaticViewSitemap}},
        name="django.contrib.sitemaps.views.sitemap",
    ),
]
