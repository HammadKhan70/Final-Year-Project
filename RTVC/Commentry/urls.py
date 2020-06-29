from django.contrib import admin
from django.urls import path
from Commentry import views
from django.contrib.auth.views import LoginView

# this is a application urls file

urlpatterns = [

    path("", views.index, name='commentry'),
    path("index", views.index, name='index'),
    path("about", views.about, name='about'),
    path("contact", views.contact, name='contact'),
    path("News", views.News, name='News'),
    path("News1", views.News1, name='News1'),
    path("TeamRanking", views.TeamRanking, name='TeamRanking'),
    path("login", views.login, name='login'),
    path("signup", views.signup, name='signup'),
    path("display", views.display, name='display'),
    path("logout", views.logout, name='logout'),
    #path("home", views.home, name='home'),
    path("speech", views.speech, name='speech'),



]

# Ctrl+K+C for comment
# Ctrl+K+U for uncomment
