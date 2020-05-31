from django.contrib import admin
from django.urls import path
from Commentry import views

# this is a application urls file

urlpatterns = [
    path("", views.index, name='commentry'),
    path("about", views.about, name='about'),
    path("contact", views.contact, name='contact'),
    path("News", views.News, name='News'),
    path("News1", views.News1, name='News1'),
    path("TeamRanking", views.TeamRanking, name='TeamRanking'),
    path("login", views.login, name='login'),
    path("signup", views.signup, name='signup'),
    path("display", views.display, name='display'),


]

# Ctrl+K+C for comment
# Ctrl+K+U for uncomment
