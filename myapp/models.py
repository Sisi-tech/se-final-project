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
    
class User(models.Model):
    team_name = models.ForeignKey(TeamInfo, on_delete=models.PROTECT, default=None)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=11)
    co_first_name = models.CharField(max_length=200)
    co_last_name = models.CharField(max_length=200)
    co_email = models.EmailField(max_length=200)
    co_phone = models.CharField(max_length=11)
    def __str__(self):
        return f"Captain: {self.first_name} {self.last_name} & {self.co_first_name} {self.co_last_name}"
    
class Player(models.Model):
    team_name = models.ForeignKey(TeamInfo, on_delete=models.PROTECT, default=None)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=11)
    def __str__(self):
        return f"Player: {self.first_name} {self.last_name}"

class Waiver(models.Model):
    team_name = models.ForeignKey(TeamInfo, on_delete=models.PROTECT, default=None)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    date = models.DateField()
    def __str__(self):
        return self.first_name + " " + self.last_name


