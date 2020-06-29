from django.contrib import admin
from .models import news
from .models import recent_matches
from .models import top_scores
from .models import league_table
from .models import game_schedule
from .models import display_ad
from .models import upcoming_matches
from .models import team_squad
from .models import homepage_news
from .models import score
from .models import music

# Register your models here.

admin.site.register(news)
admin.site.register(recent_matches)
admin.site.register(top_scores)
admin.site.register(league_table)
admin.site.register(game_schedule)
admin.site.register(display_ad)
admin.site.register(upcoming_matches)
admin.site.register(team_squad)
admin.site.register(homepage_news)
admin.site.register(score)
admin.site.register(music)
