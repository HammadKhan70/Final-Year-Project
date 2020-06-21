from django.db import models

# Create your models here.


class news(models.Model):

    month = models.CharField(max_length=100)
    day = models.IntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    desc = models.TextField()
    img = models.ImageField(upload_to='images')


class recent_matches(models.Model):

    date_time = models.CharField(max_length=200)
    img1 = models.ImageField(upload_to='images')
    img2 = models.ImageField(upload_to='images')
    team1 = models.CharField(max_length=100)
    team2 = models.CharField(max_length=100)
    team1_over = models.PositiveIntegerField()
    team2_over = models.PositiveIntegerField()
    team1_score = models.PositiveIntegerField()
    team2_score = models.PositiveIntegerField()
    team1_out = models.IntegerField(blank=True, null=True)
    team2_out = models.IntegerField(blank=True, null=True)


class top_scores(models.Model):

    img = models.ImageField(upload_to='images')
    player_name = models.CharField(max_length=100)
    games = models.PositiveIntegerField()
    score = models.PositiveIntegerField()


class league_table(models.Model):

    team_name = models.CharField(max_length=100)
    matches = models.PositiveIntegerField()
    win = models.PositiveIntegerField()
    lost = models.PositiveIntegerField()
    points = models.PositiveIntegerField()
    net_run_rate = models.DecimalField(
        default=0.00, max_digits=100, decimal_places=4)


class game_schedule(models.Model):

    date_place = models.CharField(max_length=100)
    team1_img = models.ImageField(upload_to='images')
    team2_img = models.ImageField(upload_to='images')
    team1 = models.CharField(max_length=100)
    team2 = models.CharField(max_length=100)


class display_ad(models.Model):

    img_ad = models.ImageField(upload_to='images')
    title = models.CharField(max_length=150)
    description = models.TextField()


class upcoming_matches(models.Model):

    image1 = models.ImageField(upload_to='images')
    image2 = models.ImageField(upload_to='images')
    place_date = models.CharField(max_length=100)
    team1_name = models.CharField(max_length=100)
    team2_name = models.CharField(max_length=100)


class team_squad(models.Model):

    player_image = models.ImageField(upload_to='images')
    player_name = models.CharField(max_length=100)
    player_desc = models.CharField(max_length=100)


class homepage_news(models.Model):

    month = models.CharField(max_length=100)
    day = models.IntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    desc = models.TextField()
    img = models.ImageField(upload_to='images')


class score(models.Model):

    image_team1 = models.ImageField(upload_to='images')
    image_team2 = models.ImageField(upload_to='images')
    name_team1 = models.CharField(max_length=100)
    name_team2 = models.CharField(max_length=100)
