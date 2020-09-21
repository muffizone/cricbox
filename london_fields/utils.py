import datetime
from django.db.models import Q

FIFTIES = Q(Q(runs__gt=49), Q(runs__lte=99))
HUNDREDS = Q(runs__gt=99)
FIVERS = Q(Q(wickets__gt=4))

TABLE_ATTRS = {"class": "table table-striped table-bordered table-hover",
               "thead": {
                   "class": "thead-light"
                   }
               }

SITE_URLS = {
    "LONDON_FIELDS_MAP_URL": "http://maps.google.co.uk/maps?f=q&source=s_q&hl=en&q=Martello+St,+Hackney,+London+E8,"
                             "+United+Kingdom&sll=53.800651,-4.064941&sspn=19.910905,39.418945&ie=UTF8&cd=1&"
                             "geocode=Ff94EgMdlR3__w&split=0&safe=on&ll=51.542559,-0.06006&spn=0.005098,"
                             "0.009624&t=h&z=17",
    "VPCCL_LEAGUE_TABLES_URL": "http://www.vpccl.co.uk/fixtures+results/2012/teams/londonfields.html",
    "VPCCL_URL": "http://www.vpccl.co.uk",
    "NELCL_URL": "http://www.nelcl.com/",
    "NELCL_RULES": "https://nelcl.leaguerepublic.com/l/newsArticle/nelcl_rules_2019.html",
    "NELCL_SCORECARD_PROCEDURES": "https://nelcl.leaguerepublic.com/l/newsArticle/match_report_procedure.html",
    "LONDON_FIELDS_SHED_RULES": "https://drive.google.com/file/d/145DTbtkD8e2SBZYsUFXy8ytqMHUaOmVV/view",
    "PUB_ON_THE_PARK_URL": "http://www.pubonthepark.com/",
    "LONDON_FIELDS_INSTAGRAM_PAGE": "https://www.instagram.com/londonfieldscc/",
    "YEAR": datetime.datetime.now().year
    }