from django.shortcuts import render, HttpResponse
from .models import news

# Create your views here.


def index(request):

    return render(request, 'index.html', {'score': 300})
   # return HttpResponse("this is Hammad Khan Baloch")


def about(request):
    return render(request, 'about.html')
   # return HttpResponse("this is about page")


def contact(request):
    return render(request, 'contact.html')
    # return HttpResponse("this is a services")


def News(request):

    ne1 = news()
    ne1.name = 'Australia in command despite late collapse on day three'
    ne1.desc = '2020'

    ne2 = news()
    ne2.name = 'India vs West Indies ODI series - whats at stake really?'
    ne2.desc = '2021'

    ne = [ne1, ne2]

    return render(request, 'News.html', {'ne': ne})


def News1(request):
    return render(request, 'News1.html')


def TeamRanking(request):
    return render(request, 'TeamRanking.html')


def login(request):
    return render(request, 'login.html')


def signup(request):
    return render(request, 'signup.html')


def display(request):
    return render(request, 'display.html')
