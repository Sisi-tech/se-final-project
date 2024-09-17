from django.db import models

# Create your models here.
class TeamInfo(models.Model):
    team_name = models.CharField(max_length=200, unique=True, primary_key=True)
    division_choice = [
        ('social', "Social"),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced')
    ]
    division = models.CharField(max_length=50, choices=division_choice)
    game_time_choices = [
        ('Mid', 'Mid'),
        ('Late', 'Late'),
        ('Flexible', 'Flexible')
    ]
    preferred_game_time = models.CharField(max_length=50, choices=game_time_choices)
    t_shirts_choices = [
        ('None ($0)', 'None ($0)'),
        ('Cotton ($75)', 'Cotton ($75)'),
        ('Dri-Fit ($100)', 'Dri-Fit ($100)')
    ]
    t_shirts = models.CharField(max_length=50, choices=t_shirts_choices)
    def __str__(self):
        return self.team_name
    
class TeamCaptain(models.Model):
    captain_first_name = models.CharField(max_length=200)
    captain_last_name = models.CharField(max_length=200)
    captain_email = models.EmailField(max_length=200)
    captain_phone = models.CharField(max_length=11)
    co_captain_first_name = models.CharField(max_length=200)
    co_captain_last_name = models.CharField(max_length=200)
    co_captain_email = models.EmailField(max_length=200)
    co_captain_phone = models.CharField(max_length=11)
    team_name = models.ForeignKey(TeamInfo, on_delete=models.PROTECT, default=None)
    def __str__(self):
        return f"Captain: {self.captain_first_name} {self.captain_last_name} & {self.co_captain_first_name} {self.co_captain_last_name}"
    
class TeamRoster(models.Model):
    team_name = models.ForeignKey(TeamInfo, on_delete=models.PROTECT, default=None)
    player_first_name = models.CharField(max_length=200)
    player_last_name = models.CharField(max_length=200)
    player_email = models.EmailField(max_length=200)
    player_phone = models.CharField(max_length=11)
    def __str__(self):
        return f"Team Roster: {self.player_first_name} {self.player_last_name}"

class Waiver(models.Model):
    team_name = models.ForeignKey(TeamInfo, on_delete=models.PROTECT, default=None)
    waiver_first_name = models.CharField(max_length=200)
    waiver_last_name = models.CharField(max_length=200)
    waiver_email = models.EmailField(max_length=200)
    date = models.DateField()
    def __str__(self):
        return self.waiver_first_name + " " + self.waiver_last_name


