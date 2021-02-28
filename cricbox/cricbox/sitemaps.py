# Django imports
from django.contrib import sitemaps
from django.urls import reverse


class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = "yearly"

    def items(self):
        return [
            "site-home",
            "site-about",
            "site-history",
            "site-links",
            "site-positions",
            "site-performers",
            "site-handbook",
            "site-match_manager",
            "site-stats",
            "batsmen-stats",
            "bowling-stats-all",
            "match-appearances-player",
            "fixtures-overview",
            "season-overview",
            "opposition-overview",
            "venues-overview",
            "players",
        ]

    def location(self, item):
        return reverse(item)
