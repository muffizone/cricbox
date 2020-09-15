from django.shortcuts import render
from django.http import HttpResponse
from .tables import Scorecard
import datetime
import mimetypes

LONDON_FIELDS_MAP_URL = "http://maps.google.co.uk/maps?f=q&source=s_q&hl=en&q=Martello+St,+Hackney,+London+E8," \
                        "+United+Kingdom&sll=53.800651,-4.064941&sspn=19.910905,39.418945&ie=UTF8&cd=1&" \
                        "geocode=Ff94EgMdlR3__w&split=0&safe=on&ll=51.542559,-0.06006&spn=0.005098,0.009624&t=h&z=17"
VPCCL_LEAGUE_TABLES_URL = "http://www.vpccl.co.uk/fixtures+results/2012/teams/londonfields.html"
VPCCL_URL = "http://www.vpccl.co.uk"
NELCL_URL = "http://www.nelcl.com/"
PUB_ON_THE_PARK_URL = "http://www.pubonthepark.com/"
LONDON_FIELDS_INSTAGRAM_PAGE = "https://www.instagram.com/londonfieldscc/"


# Create your views here.
def home(request):
    context = {
        'london_fields_map_url': LONDON_FIELDS_MAP_URL,
        'vpccl_league_tables_url': VPCCL_LEAGUE_TABLES_URL,
        'nelcl_url': NELCL_URL,
        'pub_on_the_park_url': PUB_ON_THE_PARK_URL,
        'instagram_page': LONDON_FIELDS_INSTAGRAM_PAGE
        }
    return render(request, "home/home.html", context)


def stats(request):
    return render(request, "home/stats.html")


def history(request):
    london_fields_scorecard = [
        {"name": "Osman", "first_innings": "5 b. Ripley", "second_innings": "6 c. Erwood"},
        {"name": "Chapman", "first_innings": "2 b. Ripley", "second_innings": "0 b. Ripley"},
        {"name": "Barber", "first_innings": "0 b. Ripley", "second_innings": "5 b. Jonson"},
        {"name": "James", "first_innings": "2 stumpt Trigg", "second_innings": "10 b. Ripley"},
        {"name": "Burrow", "first_innings": "0 st. Messenger", "second_innings": "6 c. Erwood"},
        {"name": "Lorimer", "first_innings": "3 b. Messenger", "second_innings": "5 c. Jonson"},
        {"name": "Pearce", "first_innings": "25 not out", "second_innings": "10 b. Ripley"},
        {"name": "Large", "first_innings": "1 b. Ripley", "second_innings": "6 c. Jonson"},
        {"name": "Low", "first_innings": "3 b. Ripley", "second_innings": "2 stumpt Ripley"},
        {"name": "Hoare", "first_innings": "4 b. Crisford", "second_innings": "1 run out"},
        {"name": "Yeats", "first_innings": "0 b. Messenger", "second_innings": "7 not out"},
        {"name": "Extras", "first_innings": "Byes 2", "second_innings": "Byes 3"},
        {"name": "Total", "first_innings": "47", "second_innings": "53"},
        ]
    clapton_scorecard = [
        {"name": "Glaizer", "first_innings": "16 b. Pearce"},
        {"name": "Robbin", "first_innings": "18 c. Lorimer"},
        {"name": "Hoare", "first_innings": "1 stumpt Barber"},
        {"name": "Jonson", "first_innings": "45 stumpt Osman"},
        {"name": "Messenger", "first_innings": "13 c. ditto"},
        {"name": "Prise", "first_innings": "21 c. Yeats"},
        {"name": "Crisford", "first_innings": "13 b. Pearce"},
        {"name": "Ripley", "first_innings": "4 b. Osman"},
        {"name": "Stewart", "first_innings": "2 c. Hoare"},
        {"name": "Jaines", "first_innings": "not out"},
        {"name": "Smith", "first_innings": "2 c. Osman"},
        {"name": "Extras", "first_innings": "Byes 11"},
        {"name": "Total", "first_innings": "149"}
        ]
    tables = [
        Scorecard(london_fields_scorecard),
        Scorecard(clapton_scorecard, exclude="second_innings")
        ]

    return render(request, "home/history.html", {"tables": tables})


def about(request):
    context = {
        'london_fields_map_url': LONDON_FIELDS_MAP_URL,
        'vpccl_url': VPCCL_URL,
        'nelcl_url': NELCL_URL,
        'pub_on_the_park_url': PUB_ON_THE_PARK_URL,
        'instagram_page': LONDON_FIELDS_INSTAGRAM_PAGE
        }
    return render(request, "home/about.html", context=context)


def links(request):
    return render(request, "home/links.html")


def honours(request):
    return render(request, "home/honours.html")


def handbook(request):
    context = {
        'year': datetime.datetime.now().year
        }
    return render(request, "home/handbook.html", context)


def match_manager(request):
    return render(request, "home/match_manager.html")
