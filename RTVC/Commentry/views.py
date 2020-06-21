from django.shortcuts import render, HttpResponse
from .models import news
from .models import top_scores
from .models import recent_matches
from .models import league_table
from .models import game_schedule
from .models import display_ad
from .models import upcoming_matches
from .models import team_squad
from .models import homepage_news
from .models import score
# Create your views here.


def index(request):
    home_news = homepage_news.objects.all()
    team = team_squad.objects.all()
    upcome = upcoming_matches.objects.all()
    ad = display_ad.objects.all()
    schedule = game_schedule.objects.all()

    return render(request, 'index.html', {'home_news': home_news, 'team': team, 'upcome': upcome, 'ad': ad, 'schedule': schedule})
   # return HttpResponse("this is Hammad Khan Baloch")


def about(request):
    return render(request, 'about.html')
   # return HttpResponse("this is about page")


def contact(request):
    return render(request, 'contact.html')
    # return HttpResponse("this is a services")


def News(request):
    new = news.objects.all()
    return render(request, 'News.html', {'new': new})


def News1(request):
    return render(request, 'News1.html')


def TeamRanking(request):

    recent = recent_matches.objects.all()
    top = top_scores.objects.all()
    table = league_table.objects.all()

    return render(request, 'TeamRanking.html', {'top': top, 'table': table, 'recent': recent})


def login(request):
    return render(request, 'login.html')


def signup(request):
    return render(request, 'signup.html')


def display(request):
    return render(request, 'display.html')
