from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
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
from .models import music
# speech

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
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        message = request.POST['message']

        user = User.objects.create_user(
            username=username, email=email, message=message)
        user.save()
        return redirect('contact.html')
    else:
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

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('login')

    else:
        return render(request, 'login.html')

    return render(request, 'login.html')


def signup(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username is already taken.')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(
                    request, 'Email is already taken.Use another Email.')
                return redirect('signup')
            else:
                user = User.objects.create_user(
                    username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save()
                print('user created')

        else:
            messages.info(request, 'Your password is not matching.')
            return redirect('signup')

        return redirect('/')

    else:
        return render(request, 'signup.html')


def display(request):
    return render(request, 'display.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


@csrf_protect
def speech(request):

    fil = music.objects.all()

    data = request.POST.get("fil")
    import speech_recognition as sr
    r = sr.Recognizer()

    with sr.AudioFile(data) as source:
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)

    except:
        text = "Could not understand audio"

    data = text
    return render(request, 'speech.html', {'data': data})


# speech2
